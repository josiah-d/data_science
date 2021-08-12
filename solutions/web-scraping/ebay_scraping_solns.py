from bs4 import BeautifulSoup
import os
import requests


def find_class(soup, class_string):
    '''
    helper function for getting class information out of the soup for a page
    INPUT:
        - soup, soup object for a page
        - class_string, string of class label to grab
    OUTPUT: soup result set
    '''
    return soup.findAll(class_=class_string)


def get_src(results, grab_name=False):
    '''
    get the source link for all images in a soup results object
    INPUT:
        - results: soup results object
        - grab_name: boolean
    OUTPUT: list of tuples
    '''
    img_src = []
    for elem in results:
        tag = elem.select('img')[0]
        val = tag['src']
        if grab_name:
            cur_src = (val, elem['href'].split('/')[-2])
        else:
            cur_src = (val, '')
        img_src.append(cur_src)
    return img_src


def clean_image_paths(paths, prefix='data'):
    '''
    update image paths with a new prefix
    this is a function I use to make the code runnable from a remote directory
    INPUT:
        - paths: list of strings
        - prefix: string
    OUTPUT:
        - list of strings
    '''
    fixed_paths = []
    for p in paths:
        path, name = p
        fixed_paths.append((prefix + path[1:], name))
    return fixed_paths


def save_images(paths, save_dir, urls=False):
    '''
    save images to specified directory (save_dir), if the directory does not
    exist yet it is created
    INPUT:
        - paths: list of strings
        - save_dir: str
    OUTPUT: None
    '''
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for path, name in paths:
        if urls:
            i = requests.get(path).content 
        else:
            with open(path, 'rb') as f:
                i = f.read()
        cur_path = '{}/{}{}'.format(save_dir, name, path.split('/')[-1])
        with open(cur_path,'wb') as f:
            f.write(i)


def get_all_images(soup, path, from_web=False):
    '''
    get the images from the soup of an ebay page, then save them locally
    INPUT:
        - soup: BeautifulSoup object
        - path: string
        - from_web: boolean
    OUTPUT: None
    '''
    results = soup.select('.img.imgWr2')
    images = get_src(results, from_web)
    if from_web:
        clean_images = images
        add_on = 'live_images'
    else:
        clean_images = clean_image_paths(images)
        add_on = 'images'
    images_path = '{}/{}'.format(path, add_on)
    save_images(clean_images, images_path, from_web)

if __name__ == '__main__':
    # This will need to be updated to reflect the actual path to the
    # ebay_shoes.html data file
    path = 'data/ebay_shoes.html'
    with open(path) as f:
        html_str = f.read()
    save_path = '.'
    soup = BeautifulSoup(html_str, 'lxml')
    get_all_images(soup, save_path)

    # now lets try running this on a real ebay search page
    ebay_url = 'http://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=board+games&_sacat=0'
    soup = BeautifulSoup(requests.get(ebay_url).content, 'lxml')
    get_all_images(soup, save_path, True)
