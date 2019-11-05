__author__ = 'Alexey Koledachkin'
from selenium.webdriver.common.by import By

class Locator():

#/signup?marketing_tag=qa_test_Le8KzIP57Nf00Hbb

###   Social links    ###
    RSS = "//i[@class='fa fa-rss-square']"
    YOUTUBE = "//i[@class='fa fa-youtube-square']"
    FACEBOOK = "//i[@class='fa fa-facebook-square']"
    TWITTER = "//i[@class='fa fa-twitter-square']"
###   Home page and Contact Us   ###
    LOGO = "//a[@title='Simple Toll-Free Logo']"
    SIGN_UP = "//a[@title='Go to Sign Up Page']"
    LOGIN = "//div[@class='navbar-right hidden-xs']//a[@title='Log In']"

    HOME = "//header//a[@title='Go to Home Page']"
    CONTACT_US = "//header//a[@title='Go to Contact Us Page']"
    FAQ = "//header//a[@title='Go to FAQs Page']"
    ABOUT_US = "//header//a[@title='Go to About Us Page']"
    TEL = "//tel/span"

    HOME_BUTTON = "//footer//a[@title='Go to Home Page']"
    CONTACT_BOTTOM = "//footer//a[@title='Go to Contact Us Page']"
    FAQ_BOTTOM = "//footer//a[@title='Go to FAQs Page']"
    ABOUT_BOTTOM = "//footer//a[@title='Go to About Us Page']"

###   About Us   ###
    FCC = "//a[@title='FreeConferenceCall.Com']"
    FCC_FOR_BUISNESS = "//a[@title='FreeConferenceCall.com For Business']"

###   Contact Us   ###
    NAME = "//input[@name='name']"
    EMAIL = "//input[@name='email']"
    PHONE = "//input[@name='phone']"
    COMMENTS = "//textarea[@name='comments']"
    SUBMIT = "//button[@type='submit']"
    FCC_LINK = "//a[@title='FreeConferenceCall.Com']"
    R_FIELD = "//li[text()='This value is required']"
    INVALID_EMAIL = "//li[text()='This value should be a valid email']"
    INVALID_NUMBER = "//li[text()='This value length is invalid. It should be between 10 and 17 characters long']"
    POP_UP = "//span[text()='Message sent']"

###   FAQs   ###
    SUBMIT_TROUBLE = "//a[@title='Go to Trouble Ticket Page']"
    REFER_FRIEND = "//a[@title='Go to Refer a Friend Page']"
    INSTRUCTION = "//a[@title='Go to Instructions Page']"


###   Submit Trouble Ticket   ###
    NAME_FIELD = "//input[@id='name']"
    EMAIL_FIELD = "//input[@id='email']"
    PHONE_NUMBER = "//input[@id='phonenumber']"
    CONTACT_PREFERENCE_EMAIL = "//input[@value='Email']"
    CONTACT_PREFERENCE_PHONE = "//input[@value='Phone']"
    CONFERENCE_DATE = "//input[@id='confdate']"
    CONFERENCE_TIME = "//input[@id='conftime']"
    DIAL_NUMBER = "//input[@name='dialin_number']"
    ACCESS_CODE = "//*[@id='access_code_forgot']"
    CARRIER = "//select[@name='carrier']" # SELECT
    PHONE_TYPE = "//select[@name='phonetype']" # SELECT
    SUBJECT = "//select[@name='subject_type']" # SELECT
    DETAILS = "//textarea[@name='details']"

###   Refer a friend   ###
    FRIEND_NAME = "//input[@name='friend_name']"
    FRIEND_EMAIL = "//input[@name='friend_email']"
    YOUR_NAME = "//input[@name='your_name']"
    YOUR_EMAIL = "//input[@name='Your Email']"

###   Sign Up   ###
    FIRST_NAME = "//input[@placeholder='First Name']"
    LAST_NAME = "//input[@placeholder='Last Name']"
    PHONE_NUM = "//input[@name='phonenumber']"
    COMPANY_NAME = "//input[@placeholder='Company Name']"
    CARD_TYPE = "//select[@name='credit_card[payment]']" # SELECT
    CARD_NUMBER = "//input[@placeholder='Card Number']"
    MM = "//select[@name='credit_card[expiration_month]']" # SELECT
    YYYY = "//select[@name='credit_card[expiration_year]']" # SELECT
    CVV = "//input[@placeholder='CVV']"
    CARD_HOLDER_NAME = "//input[@placeholder='Card Holder Name']"
    TERMS_CONDITIONS = "//input[@name='agree']"
    STREET_ADDRESS = "//input[@placeholder='Street Address']"
    SUITE = "//input[@placeholder='Suite']"
    CITY = "//input[@placeholder='City']"
    STATE = "//select[@name='state']" # SELECT
    ZIP = "//input[@name='zip']"
    SAME_ABOVE = "//input[@name='billingsamecontact']"
    LOG_OUT = "//a[text()='Log out'][1]"


    SIGNUP_TOLL = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[1]"
    SIGNUP_ACCESS = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[3]"
    SIGNUP_PIN = "/html/body/div[4]/div[1]/div[1]/div/div[2]/dl[2]/dd[4]"




###   Email   ###
    PIN_LETTER = "//*/table[3]/tbody/tr/td[2]/table/tbody/tr/td"

    TEST_LOGIN_EMAIL = "//input[@name='login']"
    TEST_SUBMIT_BUTTON = "//button[@type='submit']"
    TEST_PASSWORD_EMAIL = "//input[@name='passwd']"

    CHECKBOX_CLEAR = "//span[@class='checkbox_view']"
    DELETE = "//span[text()='Удалить']"

    THANK_YOU = "//h1[text()='Thank you for signing up with SimpleTollFree']"

    EMAIL_ACCESS_CODE = "//table[2]/tbody/tr/td[2]/table/tbody/tr/td"
    EMAIL_HOST_PIN = "//table[3]/tbody/tr/td[2]/table/tbody/tr/td"
    EMAIL_NUMBER = "//table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/a/span"

    PROF_STATE_LOCATOR = "//select[@name='subscription[state]']/option[@value='Arizona']"

###   Login   ###
    HOST_PIN = "//input[@name='subscriber_pin']"
    REMEMBER_ME = "//input[@name='rememberme']"
    ACCESSCODE = "//input[@name='access_code']"

    PAGE_NAME = "//h1[text()='Account Information']"
    FORGOT_PASS = "//a[@id='forgot_pin']"
    SEND_INFO = "//button[text()='Send Info']"

    ALERT = "//span[text()='Your account info has been emailed to smcallacc@gmail.com']"

###   Account information   ###
    TOLL = "//dd[1]"

    TOLLFREE = "//dd[2]"
    ACC_ACCESSCODE = "//dd[3]"
    ACC_HOSTPIN = "//dd[4]"

    ACC_PLAYBACK_NUMBER = "//dd[5]"

    ACC_EMAIL = "//input[@name='subscription[email]']"
    ACC_FIRST_NAME = "//input[@placeholder='First Name']"
    ACC_LAST_NAME = "//input[@placeholder='Last Name']"
    ACC_PHONE_NUM = "//input[@placeholder='Phone Number']"
    ACC_COMPANY_NAME = "//input[@placeholder='Company Name']"

    ACC_STREET_ADDRESS = "//input[@placeholder='Street Address']"
    ACC_SUITE = "//input[@placeholder='Suite']"
    ACC_CITY = "//input[@placeholder='City']"
    ACC_STATE = "//select[@name='subscription[state]']" # SELECT
    ACC_ZIP = "//input[@placeholder='Zip']"

    DRP_TIMEZONES = "//select[@id='timezones']"
    ACC_TIMEZONES = "//select[@id='timezones']"
    ACC_CHANGE_ZONES = "//button[@id='toggle-tz']"
    ACC_RESEND_INFO = "//button[text()='Resend Info']"
    RESEND_INFO_MESSAGE = "//span[text()='Information has been resend successfully']"


###   History and recordings   ###

    START_DATE = "//input[@placeholder='Start Date']"
    END_DATE = "//input[@placeholder='End Date']"
    TYPE_CONFERENCE = "//select[option]"
    SEARCH = "//button[text()='Search']"

    ### Sorting
    SORT_BY_DATE_TIME = "//div[text()='Start Date/Time']"
    SORT_BY_END_TIME = "//div[text()='End Time']"
    SORT_BY_CALLERS = "//div[text()='Callers']"
    SORT_BY_DURATION = "//div[text()='Duration']"
    SORT_BY_RECORDING_OPTIONS = "//div[text()='Recording Options']"
    SORT_BY_SIZE = "//div[text()='Size']"

    ### Work with table
    OPEN_RECORDING = "//i[@class='fa fa-plus icon-plus'][1]"
    CLOSE_RECORDING = "//i[@class='fa fa-minus icon-minus'][1]"

    DOWNLOAD = "//i[@class='fa fa-download fa-lg']"
    PLAY = "//i[@class='fa fa-play fa-lg']"
    TRASH = "//i[@class='fa fa-trash fa-lg']"

    PAUSE = "//a[text()='pause']"
    PLAY_BUTTON = "//a[text()='play']"
    STOP = "//a[text()='stop']"
    MUTE = "//a[text()='mute']"
    UNMUTE = "//a[text()='unmute']"
    CURRENT_TIME = "//div[@id='currentTime']"
    REPEAT = "//a[text()='repeat']"
    REPEAT_OFF = "//a[text()='repeat off']"
    DOWNLOAD_PDF = "//a[text()='Download PDF']"

###   Titles   ###

    LOGIN_TITLE = "Account Information - SimpleTollFree"
    ACCOUNT_INFO = "Account Information - SimpleTollFree"
    RECORDINGS = "History & Recordings - SimpleTollFree"
    YANDEX_PAGE = "https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1"




