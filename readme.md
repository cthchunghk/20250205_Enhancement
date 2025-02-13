Please install ffmpeg for downloading youtube track     

## How To Run
- Create Virtual Environment First:
    >python -m venv ${PROJECT_ROOT}

- Activate Virtual Environment
    * Windows:
        >.\venv\Scripts\activate.ps1     

        OR
        >.\venv\Scripts\activate.bat
    * Mac / Linux:
        >. ./venv_flask/bin/activate

- Install dependencies      
    After Activated the VEnv, run:
    >pip install -r .\req.txt

- Ready OpenAI API key      
    Create a .env file in the project root, insert the following key:
    >APIKEY=YOUR_API_KEY

- Run Server        
    For Development:
    ```
    flask --app app.main run --debug
    ```

## API Spec:
### All Use "POST" only

- /api/summary      
    To create summary by OpenAI         
    Receive Parameter:
    ```
    {
        "text": {Text you want to summarize} 
    }   
    ```  
   
    Return Format:      
    ```
    {
        "status": "success",      
        "create_time": "{Request finished time}",        
        "payloads": [
            {       
            "title": "{title based on the provided Text}",      
            "summary": "{Text Summarized}"
            }
        ]
    }
    ``` 


- /api/response/text   
    To create response from OpenAI based on Q&A list
    Receive Parameter:      
    ```
    {
        "question": {question provided by user} 
    }
    ```

    Return Format:
    ```
    {
        "status": "success",      
        "create_time": "{Request finished time}",       
        "payloads": [       
            {       
                "question": "{question provided by user}",      
                "response": "{Response created by OpenAI based on Q&A list}"
            }       
        ]       
    }
    ```


- /api/download/clip     
    To download the clip and convert to mp3 audio       
    Receive Parameter:
    ```
    {
        "url": "{the YouTube link}"
    }      
    ```

    Return Format:
    ``` 
    {
        "status": "success",      
        "create_time": "{Request finished time}",         
        "payloads": [       
            {       
                "store_path": "{The path saved the audio, should be local path}"        
            }       
        ]       
    }       
    ```


- /api/transcript              
    To transforming audio to text by OpenAI. Currently only supports input saved voice file           
    Receive Parameter:
    ```
    {
        "file_path": "{The audio file path}"
    }
    ``` 
    Return format:
    ```
    {
        "status": "success",
        "create_time": "{Request finished time}",
        "payloads": [
            {
                "script": "{The text OpenAI model transcribed}"
            }
        ]
    }
    ```


- /api/response/speech              
    Read a loud from provided text by OpenAI. It is costly now.     
    Receive Parameter:
    ```
    {
        "text": "{The text you want to read a loud}"
    }
    ```    
    Return format:
    ```
    {
        "status": "success",
        "create_time": "{Request finished time}",
        "payloads": [
            {
                "file_path": "{The path saving speech file, should be a local path}"
            }
        ]
    }
    ```

- /api/scrape/page              
    Scrape single page.     
    Receive Parameter:
    ```
    {
        "url": "{The path you want to scrape}"
    }
    ```    
    Return format:
    ```
    {
        "status": "success",
        "create_time": "{Request finished time}",
        "payloads": [
            {
                "page_detail": {
                    "url": "{The URL to scrape}",
                    "title": "{The title of the webpage}",
                    "content": "{The text in the webpage}"
                }
            }
        ]
    }
    ```
                
- /api/scrape/all       
    Scrape all the page can be discovered in provided URL. Very slow. Use with caution.         
    Receive Parameter:
    ```
    {
        "url": "{The path you want to scrape}"
    }
    ```    
    Return format:
    ```
    {
        "status": "success",
        "create_time": "{Request finished time}",
        "payloads": [
            {
                "page_detail": [
                    {
                        "url": "{The URL scraped}",
                        "title": "{The title of the webpage}",
                        "content": "{The text in the webpage}"
                    },
                    {
                        // And go on...
                    }
                ]
            }
        ]
    }
    ```
