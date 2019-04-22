## es que no me convence nada de nada
def getFromReddit():
    url = 'https://www.reddit.com/r/spaceporn.json'
    response = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    if not response.ok:
        print("Error", response.status_code)
        exit()
    data = response.json()['data']['children']
    # get first post from array of posts
    first_post = data[0]['data']
    # get the image url of the first post
    image_url = first_post['url']
    if '.png' in image_url:
        extension = '.png'
    elif '.jpg' in image_url or '.jpeg' in image_url:
        extension = '.jpeg'
    else:
        image_url += '.jpeg'
        extension = '.jpeg'
    # prevents thumbnails denoting removed images from being downloaded
    image = requests.get(image_url, allow_redirects=False)
    if(image.status_code == 200):
        try:
            path = getPath()
            print(path)
            output_filehandle = open(path+first_post['title'] + extension, mode='bx')
            output_filehandle.write(image.content)
        except:
            pass
#    print(data)
