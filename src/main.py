# import openai
# import cv2
from dotenv import load_dotenv
import TextReader
import AITutorWebsite


def main():
    website = AITutorWebsite.AITutorWebsite()

#------------ Driver Code --------------
load_dotenv("../.env")
main()
# cgpt = "a^2 + b^2 = c^2"
# TextReader.talk(cgpt)