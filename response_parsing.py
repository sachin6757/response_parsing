import urllib2
import json

def count():


# Variable to store headers
    request_headers = {
"Accept-Language": "en-US,en;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
"Accept": "*/*",
"Content-Type": "text/plain; charset=utf-8"
}
    
    page =1  # variable to store page number
    cntresptrue=0 # variable to store count of response object with hd flag true
    cntrespfalse=0 # variable to store count of response object with hd flag false
    more=True # variable to store "more" value from response
    
    #While loop till the "more" value is false
    while(more):


        
        url = "http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page="+str(page)

        
        #make api request with the page number and read response
        request = urllib2.Request(url, headers=request_headers)
        contents = urllib2.urlopen(request).read()

        #validates the json response
        json_response = json.loads(contents)

        #Verify if "more" is flase then set more to false
        if json_response['more'] != True:
            more = False
            
        #if "more" is true then increment page number
        page = page + 1
        
        #for loop to go through all the response objects
        for i in json_response['response']:
            if i['flags']['hd'] == True:
                cntresptrue = cntresptrue + 1 #if hd is true then increment count
            elif i['flags']['hd'] == False:
                cntrespfalse = cntrespfalse + 1 #if hd is false then increment count
 
    print "Total no. of response object with hd flag true: %s" %cntresptrue

    print "Total no. of response object with hd flag false: %s" %cntrespfalse

    

if (__name__=="__main__"):
    count()
