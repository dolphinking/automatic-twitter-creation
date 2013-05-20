import mechanize, sys, lxml, urllib
from lxml.html import document_fromstring
from PIL import Image

def createAccount():
	name = sys.argv[1]
	mail = sys.argv[2]
	pw = sys.argv[3]


	br = mechanize.Browser()
	site = br.open("https://mobile.twitter.com/signup")
	tree = document_fromstring(site.read())
	img = tree.xpath('//div[@class="captcha  "]/img')
	if (len(img) < 1):
		print "Found no Captcha - something is wrong."
		return
	urllib.urlretrieve (img[0].attrib['src'], "captcha.gif")
	img = Image.open('captcha.gif')
	img.show()

	br.select_form(nr=0)
	br['oauth_signup_client[fullname]'] = name
	br['oauth_signup_client[phone_number]'] = mail
	br['oauth_signup_client[password]'] = pw
	captcha = raw_input('Please solve the Captcha - I can not do that for you :(:\n')
	br['captcha_response_field'] = captcha

	print br.submit().read()

if len(sys.argv)<2:
	print "First: Full Name"
	print "Second: Email"
	print "Third: Password"
else:
	createAccount()