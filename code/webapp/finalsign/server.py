import http.server
import socketserver
import os
from urllib.parse import unquote
from sign_dictionary import sign_dictionary
import random as tts

    # Serve files from the current directory
DIRECTORY = "."
print(sign_dictionary)
class SignLanguageHandler(http.server.SimpleHTTPRequestHandler):
        
        def do_GET(self):
            # Check if the request is for a video\
            print("does it reach here ???????")
            if self.path.startswith("/get_video/"):
                print("does it reach here ??????? PART 2")
            # Extract the word after "/get_video/"
                word = unquote(self.path[len("/get_video/"):].strip("/"))
                print("does it reach here ??????? PART 3")
                video_path = sign_dictionary.get(word)
                
                if video_path and os.path.exists(video_path):
                    # Serve the video file
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(video_path.encode())
                else:
                    # Respond with 404 if video not found
                    # self.send_response(404)
                    # self.end_headers()
                    # self.wfile.write(f"Video for word '{word}' not found.".encode())

                    key,val = tts.choice(list(sign_dictionary.items()))
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(val.encode())
                    
            else:
                # Serve other files (HTML, JS, CSS)
                super().do_GET()

    # Set the port and directory for the server
PORT = 8000
os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), SignLanguageHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
