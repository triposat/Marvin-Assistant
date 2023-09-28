![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/Mini_Assistant?color=red&label=Repo%20Size%20)
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatyam/Mini_Assistant?color=red&label=Lines%20of%20Code)
![License](https://img.shields.io/badge/License-MIT-red.svg)</br>
![](https://profile-counter.glitch.me/{Mini_Assistant}/count.svg)

<p align="center">
<a href="https://github.com/Iamtripathisatyam/Mini_Assistant/blob/main/Content/code.py"><img width="20%" src="https://user-images.githubusercontent.com/69134468/128800245-60875112-29c5-4801-8023-e9d84a834b24.png" /></a>
</p>

- [Introduction](#Intro)
- [What can Assistant do?](#do)
  - [Wish you (Good Morning, Good Afternoon, and Good Evening) according to time](#wish) 
  - [Search on Wikipedia](#wiki)
  - [Search on YouTube](#you)
  - [Search on Google](#goog)
  - [Send Email](#mail)
  - [Keep Notes](#notes)
  - [Time](#time)
  - [Date](#date)
  - [Play Music](#music)
  - [Send Notifications](#noti)
  - [Maths Calculations](#maths)
  - [Words Meaning](#words)
  - [Weather Notifications](#weath)
  - [Battery of your PC](#batt)
  - [ShutDown your PC](#shut)
  - [Search Locations](#locate)
  - [Download Video](#download)
  - [Tell Jokes](#joke)
  - [reSTART](#restart)
  - [Take a Photo](#photo)
  - [Empty Recycle Bin](#bin)
- [Contribute](#contribute)
- [Output](#out)
- [Conclusion](#conc)

## Introduction:<a name="Intro"></a>
This project can do any web-related activity effectively, such as sending emails, searching on YouTube and Google, locating places, telling a joke, sending alerts to your phone, battery-related notifications, and so on.

When we run the code, it will display an appealing interface with several options and a next button. Following that, you will see a ***search box*** where you can input anything you want, such as google, wikipedia, and so on.

If you enter spelling that does not exist, it will display an error message, and you will be unable to continue. It will display ***successful messages***, ***warning messages***, and ***pop-up messages*** for any information.

## What can Assistant do?<a name="do"></a>
- ### Wish you: <a name="wish"></a>
  - It will wish you according to the time, using the ***datetime*** module.
  - Using the below code, it will first calculate an hour.
    
    ```python
    hour = int(datetime.datetime.now().hour)
    ```
  - Following that, it will use some if-and-else loops to determine the ideal timing for the wishes.
    
    ```python
    if hour >= 5 and hour < 12:
        print("Good Morning")
    elif hour >= 12 and hour < 17:
        print('Good Afternoon')
    else:
        print('Good Evening')

    ```
- ### Search on Wikipedia:<a name="wiki"></a>
  - It will first ask the user for input, and with the help of the ***Wikipedia*** module, it performs all the operations.
    
    ```python
    Test_string = input(placeholder="Wikipedia Search", required=True)
    ```
  - It will initially seek input from the user. It will now check to see whether if the input exists in Wikipedia. If it's in Wikipedia, we'll try to get a summary by providing some relevant keywords.
    
    ```python
      Result = wikipedia.summary(Test_string, sentences=2, auto_suggest=False, redirect=True)
    ```
  - If it isn't found on Wikipedia, the suggested keywords will be searched using the approach described below.
    
    ```python
    Test_string = wikipedia.suggest(Test_string)
    ```
- ### Search on YouTube: <a name="you"></a>
  - It will first ask the user for input, and with the help of the ***Webbrowser*** module, it performs all the operations.
    
    ```python
    Test_string = input(placeholder="YouTube Search", required=True)
    ```
  - For searching on YouTube, it will now use the ***open*** function specified in the webbrowser module.
   
    ```python
    webbrowser.open(f"https://www.youtube.com/results?search_query={Test_string}")
    ```
- ### Search on Google:<a name="goog"></a>
  - It will first ask the user for input, and with the help of the ***Webbrowser*** module, it performs all the operations.

    ```python
    Test_string = input(placeholder="YouTube Search", required=True)
    ```
  - For searching on Google, it will now use the ***open*** function specified in the webbrowser module.

    ```python
    webbrowser.open(f"https://www.youtube.com/results?search_query={Test_string}")
    ```
- ### Send Emails:<a name="mail"></a>
  - **Register User Email ID:** By registering, we allow the yagmail to access our Gmail account in consent to send emails. There is a need for an SMTP client to provide the authentication to the client for sending an email.  
  
    ```python
    yagmail.register("Sender’s Gmail Username", "Sender’s Gmail Password")
    ```
  - **Connect to SMTP server:** To initiate a connection with the SMTP server using the SMTP client, use the command below.
    
    ```python
    yag = yagmail.SMTP(“Sender@gmail.com”)
    ```
  - **Adding Content and Delivering:** 
     - In 1st argument in send() function, pass the receiver’s email address.
     - Then in the 2nd one, pass the Subject of the Mail your sender is sending.
     - Now in the 3rd one, pass the  Content of Mail i.e text or media.
     </br>
     
     ```python
      yag.send(“Reciever@gmail.com”,”Subject Of Mail”,”Content(Text, Media etc)”)
      ```
   
- ### Keep Notes: <a name="notes"></a>
    - For creating a new note, you need to give a **title** for a note and the **contents** to be noted.
    - The assistant uses **SQLAlchemy**, a database library which uses **SQLite** in the backend, to store and keep track of the notes
    - If you need to view a note, you need to enter only the title of the note. After entering the title, the contents of the note will be displayed.
    - **Creating the database:**</br>

	    ```python
	    engine = db.create_engine('sqlite:///notes.db')
	    metadata = db.MetaData()
	    notes = db.Table('notes', metadata, db.Column('Time', db.String(255), nullable=False, primary_key=True), db.Column(
		 'Title', db.Text(), nullable=False, primary_key=True), db.Column('Note', db.Text(), default=''))
	    metadata.create_all(engine)
	    ```
    - **Enterting a note:** While entering a note, this function gets invoked and the new note is saved in the database.</br>
    
	    ```python
	    def enterNote(title,note):
	    current_dateTime = str(datetime.now())
	    try:   
		connection = engine.connect()     
		query = db.insert(notes).values(Time=current_dateTime,Title=title,Note=note)
		result = connection.execute(query)
		connection.close()
	    except Exception as e:
		print(e)
	    ```
    - **Viewing a note:** While we need to view a note, this function gets invoked and the note is displayed.</br>
    
	    ```python
	    def displayNote(title):
	    try:
		connection = engine.connect()
		s = notes.select().where(notes.columns.Title==title)
		result = connection.execute(s)
		for row in result:
		    print(row[2])
		connection.close()

	    except Exception as e:
		print(e)
	    ```
        
- ### Time: <a name="time"></a>
    - To find the current time, we'll use the ***datetime*** module.
    - We may simply find time using the approach outlined below.
      
      ```python
      datetime.datetime.today().strftime("%I:%M %p")
      ```
- ### Date: <a name="date"></a>
  - To find the current date, we'll use the ***datetime*** module.
  - Now, we will simply use ***%m*** to get the month number, and then we will use ***%b*** to get the month name. 
  </br>
  
     ```python
    current_time = datetime.datetime.now()
    datetime_object = datetime.datetime.strptime(str(current_time.month), "%m")
    month_name = datetime_object.strftime("%b")
     ```
 - ### Play music: <a name="music"></a>
    - You just need to enter the name of the song or music (without spaces).
    - In a matter of seconds, the assistant can play the exact song or music.
    - For this, we have used the libraries **Pytube** for accessing the songs/music and **Playsound** for playing the song/music.
    - Generating the URL of the song from the song name:</br>
    
	    ```python
	    def generateURL(songName):	
		    search_keyword= str(songName)
		    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
		    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
		url = "https://www.youtube.com/watch?v=" + video_ids[0]
	    ```
    - After the generation of the song URL, we can play the song using it: </br>
    
	    ```python
	    def playSong(url):
	      yt = YouTube(str(url))
	      audio = yt.streams.filter(only_audio=True).first()
	      out_file = audio.download()
	      base, ext = os.path.splitext(out_file)
	      new_file = base + '.mp3'
	      os.rename(out_file, new_file)
	      playsound(new_file)
	    ```
    
 - ### Send Notification:<a name="noti"></a>
    - Go to ***Pushbullet*** and obtain the access token.
    - Get your Access Token and use the PushBullet method to create an instance by providing the Access Token in the PushBullet function.
    
      ```python
      PushBullet(access_token)
      ```
   - Use the push_note function to send data and text inside the function. ***push_note*** will take two arguments i.e. data and text. the first argument will work as a Heading in the notification where 2nd argument is a text.
   
       ```python
       pb.push_note(data, text)
       ```
- ### Maths Calculations: <a name="maths"></a>
    - The assistant can perform many sorts of mathematical calculations. It will act as verbal calculator
    - **Arithmetic operations**: addition,subtraction,multiplication,division and finding the square root
    - **Trignometrical operations**: sin,cos and tan

	    **Examples**:
	    ```
	    command: Hey jarvis, add 5 and 5
	    output : 10

	    command: Hey jarvis, find the product of 6 and 5
	    output : 30

	    command: Hey jarvis, find the square root of 169
	    output : 13

	    command: Hey jarvis, find the sin of 90 degrees
	    output : 1.0
	    ```
- ### Words Meaning:<a name="words"></a>
  - Load the ***JSON*** data
    
    ```python
    json.load(open(r"C:\Users\Dell\Downloads\ebooks.json"))
    ```
  - To return the definition of the word(entered by user).
  - This function will give an appropriate message, if the word doesn't exist in the data.
  - If user will enter a word with wrong spelling, then we have to give an appropriate message using ***get_close_matches()*** function.

- ### Weather Notifications:<a name="weath"></a>
  - Firstly, get the ***API*** key from [**OpenWeather.org**](https://openweathermap.org/) to begin extracting data.
  - User need to create an account on [**OpenWeather.org**](https://openweathermap.org/), then only can use the APIs. 
    
    ```python
    api_key = "Your API Key"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    ```
  - Take City name as input and check whether city name is valid or not, and ***required=True*** means field can't be empty.
  - Extract all the data including ***Temperature***, ***Pressure***, ***Humidity***, ***Weather***, and ***Description***.

- ### Battery:<a name="batt"></a>
  - The ***psutil*** function will be used to perform battery-related tasks.
  - First, using the method outlined below, collect all the necessary information about the battery's present state.
  
    ```python
    battery = psutil.sensors_battery() # sbattery(percent=93, secsleft=19845, power_plugged=False)
    ```
  - After that we will only extract the battery with the uwse of battery function.
    
    ```python
    percent = battery.percent
    ```
  - Check whether the plug is plugged in or not.
    
    ```python
    pluged = battery.power_plugged
    ```
- ### ShutDown:<a name="shut"></a>
  - Shutting down the PC is a straightforward process that can be done with the help of the OS module.
  - The code below will shut off your computer.
    
    ```python
    os.system("shutdown /s /t  1")
    ```
- ### reSTART:<a name="restart"></a>
  - reSTARTing down the PC is also a straightforward process that can be done with the help of the ***OS*** module.
  - The code below will shut off your computer.
    
    ```python
    os.system("shutdown /r /t  1")
    ```
- ### Search Locations:<a name="locate"></a>
  - With the help of the ***webbrowser*** module, we can simply search for any place.
  - If a place exists, the code below will look for it.
    
    ```python
    webbrowser.open_new_tab("https://www.google.com/maps/place/"+what)
    ```
    
- ### Download video: <a name="download"></a>
   - You can download any Youtube video with its URL.
   - Just enter the URL of the Youtube video and the video gets downloaded.
   - It will be saved in the default **Downloads** folder in your System
   - A library called **Pytube** is used to download the video.

	  ```python
	  def downloadYTVideo(url):
	    try:
		youtube = pytube.YouTube(url)
		video = youtube.streams.filter(progressive=True,file_extension='mp4').desc().first()
		path = str(os.path.join(Path.home(),'Downloads')
		video.download(output_path=path)
	    except Exception as e:
		print(e)
	   ```

- ### Jokes:<a name="joke"></a>
  - We will use the ***pyjokes*** module for this.
  - The ***get_joke*** function is defined in the pyjokes module: simply pass the *language*and *category* of the joke.
  
    ```python
    pyjokes.get_joke(language="en", category="neutral")
    ```
- ### Take a Photo:<a name="photo"></a>
  - The ***OpenCV*** module will be used to capture the images.
  - We will capture an image using the ***VideoCapture*** function specified in ***Opencv*** and read the pixels of the picture using the ***read*** function.
    
    ```python
    camera = cv2.VideoCapture(0)
    _, image = camera.read()
    ```
  - Finally, we'll write the image and save it with a name.
    
    ```python
    cv2.imwrite(name+".png", image)
    ```
    
 - ### Empty Recycle Bin:<a name="bin"></a>
    - We'll use the ***winshell*** module to empty the recycling bin.
    - The ***recycle bin ().empty*** function in the winshell module is empty the recycle bin.
    - The code below will help us in doing this.

      ```python
      winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
      ```
## Output: <a name="out"></a>
<p align="center"><img width="80%" src="https://user-images.githubusercontent.com/69134468/128981899-4cc19a45-1919-40bf-bcda-49d39c2c2b05.PNG"></p>

## Installation:

To run the Mini Assistant project, you'll need to install some Python libraries. You can install these libraries using `pip` with the following commands:

1. pip install pushbullet.py==0.9.1

2. pip install pytube

3. pip install opencv-python

4. pip install winshell

5. pip install SQLAlchemy

6. pip install pyspellchecker

7. pip install wikipedia

8. pip install pyjokes

9. pip install psutil

10. pip install yagmail

## How to Contribute: <a name="contribute"></a>

We welcome contributions from the community to enhance and improve the Mini Assistant project. If you'd like to contribute, please follow these guidelines:

1. **Fork the Repository:**
   - Click the "Fork" button on the top right corner of this repository to create your own copy.

2. **Clone the Repository:**
   - Clone your forked repository to your local machine using the following command:
     ```
     git clone https://github.com/triposat/Marvin-Assistant.git
     ```

3. **Create a Branch:**
   - Create a new branch to work on your feature or bug fix:
     ```
     git checkout -b feature/your-feature-name
     ```

4. **Make Changes:**
   - Make your desired changes or additions to the codebase.

5. **Commit Changes:**
   - Commit your changes with a descriptive commit message:
     ```
     git commit -m "Add your commit message here"
     ```

6. **Push Changes:**
   - Push your changes to your forked repository:
     ```
     git push origin feature/your-feature-name
     ```

7. **Create a Pull Request:**
   - Go to the original repository on GitHub and click the "New Pull Request" button.
   - Provide a clear title and description for your pull request.
   - Click "Create Pull Request" to submit your changes for review.

8. **Review and Discussion:**
   - Participate in the discussion and address any feedback or questions related to your pull request.

9. **Merge Pull Request:**
   - Once your pull request is approved, it will be merged into the main project.

10. **Thank You!**
    - Thank you for contributing to Mini Assistant. Your contributions help make this project better for everyone.

If you have any questions or need assistance during the contribution process, please feel free to open an issue or reach out to us via [GitHub Issues](https://github.com/Iamtripathisatyam/Mini_Assistant/issues).

We appreciate your contributions and look forward to collaborating with you!


## Conclusion: <a name="conc"></a>
This is how easy it is to create your own desktop assistant. You may add many more functionalities, such as sending messages in Slack, providing data on Covid-19 cases, and so forth. Have fun experimenting with and creating your own Alexa/Siri/Cortana.

___________________________________

<p>&copy; 2021 Satyam Tripathi</p>
