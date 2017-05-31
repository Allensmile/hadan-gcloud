from hadan.chatbot import chatbot
import subprocess
import time

tmp_path = './'
files = 'gs://hadan-data/data.tar.xz'
furl = 'https://storage.googleapis.com/hadan-data/data.tar.xz'
idSample = 0

try:
    import random
    idSample = random.randint(0, 10000)
    subprocess.check_call(['echo', str(idSample) , '>' ,str(idSample)]  )
except Exception as e:
    pass 
    
try:
    subprocess.check_call(['gsutil', 'cp' , str(idSample) ,'gs://hadan-data/test' ]  )
except Exception as e:
    pass 
    
try:
    subprocess.check_call(['wget' ,furl ])
    pass
except Exception as e:
    pass 

try:
    subprocess.check_call(['xz', '-d' ,'data.tar.xz'] )
except Exception as e:
    pass 

time.sleep(5)  

try:
    subprocess.check_call(['mkdir', 'save']  )
except Exception as e:
    pass 
    
try:
    subprocess.check_call(['tar', 'xf' , 'data.tar'] )
except Exception as e:
    pass 
    

time.sleep(5)


chatbot = chatbot.Chatbot()
chatbot.main()


try:
    subprocess.check_call(['tar', 'cf' , 'save.tar' , 'save'  ]  )
except Exception as e:
    pass 
    
try:
    subprocess.check_call(['xz', '-z' , 'save.tar'] )
except Exception as e:
    pass 
    
   
try:
    subprocess.check_call(['gsutil', 'cp' , 'save.tar.xz' ,'gs://hadan-data/2' ]  )
except Exception as e:
    pass 
    