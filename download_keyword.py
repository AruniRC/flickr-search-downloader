import flickrapi
import requests
import argparse
import os
import os.path as osp
import tqdm

# 3rd party FlickrAPI kit: https://stuvel.eu/flickrapi

# change these with your keys after registering on FlickR
api_key = u''
api_secret = u''

OUT_DIR = './output'
PID = os.getpid()

flickr=flickrapi.FlickrAPI(api_key,api_secret,cache=True)

def flickr_walk(keyword, num_img=1000):
    photos = flickr.walk(text=keyword,
                         tag_mode='all',
                         tags=keyword,
                         extras='url_c',
                         per_page=500,
                         media='photos',
                         # is_commons=True,
                         # license='7,9,10',  
                         sort='relevance')
    # License: https://www.flickr.com/services/api/flickr.photos.licenses.getInfo.html

    img_dir = osp.join(OUT_DIR, keyword)
    if not osp.exists(img_dir):
        os.makedirs(img_dir)

    logfile = './log-%s.txt' % keyword

    count = 0
    for photo in photos:
        try:
            url = photo.get('url_c') 
            with open(logfile, 'a') as fid:
                fid.write(str(PID) + ': ' + url + '\n')

            if url is not None:
                img_data = requests.get(url).content
                im_name = url.split('/')[-1]
                with open( osp.join(img_dir, im_name), 'wb') as handler:
                    handler.write(img_data)
            count += 1
            # if count >= num_img:
            #     break
        except Exception as e:
            with open(logfile, 'a') as fid:
                fid.write('failed to download image \n')
            # print('failed to download image')


def main():
    args = parse_args()
    print 'Keyword: '  + args.keyword
    flickr_walk(args.keyword, args.num_img)


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Query Flickr API')
    parser.add_argument('-k', '--keyword', default='people')
    parser.add_argument('-n', '--num_img', default=1000)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()