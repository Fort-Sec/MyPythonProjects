import urllib.request as urllib

def main(url):
    print('Connecting.......')

    response = urllib.urlopen(url)
    print('Connected to', url, 'sucessfully')
    print('The response code:', response.getcode())

print('This is a site Connectivity checker program')
input_url = input('Input the url: ')

main(input_url)