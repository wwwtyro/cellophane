Overview
========

Typically when creating web applications, the developer must work on both client and server-side code. 
This tends to increase the amount of complexity and the number of context switches the developer must 
deal with.

One way to reduce this complexity is to make static one end of the communications and develop all 
logic on the other end. Cellophane is one attempt at implementing this paradigm, in the narrow scope 
of a 'web terminal' - a text input/output application that runs in the browser. Cellophane implements 
all of the client side code, rendering it static. This allows the developer to focus all their 
attention on the server side, never having to consider any code or logic on the client side.

Here's a simple example, an echo server:

```
import cellophane

class Echoer(cellophane.Handler):

    def on_receive(self, message):
        self.writeline(message)

cp = cellophane.Cellophane(Echoer)
cp.go()
```

If you were to run this script, Cellophane would open port 8888 on localhost and render a webpage 
there with all the logic necessary for communicating back to the server via web sockets.

Cellophane is primarily composed of two classes: Cellophane and Handler. The Cellophane class deals 
with starting up the server, while the Handler class manages the events fired by individual clients. 


The Handler class
=================

### class cellophane.Handler()

Subclass **Handler** to manage create/receive/destroy events from clients. This class is a thin wrapper 
around **tornado.websocket.WebSocketHandler**. Some functions are used internally by Cellophane and 
should not be overridden, namely:

- **\_\_init\_\_**: use **on_create** instead
- **open**: use **on_create** instead
- **on_message**: use **on_receive** instead
- **on_close**: use **on_destroy** instead

#### Methods:

**on_create**()

Called whenever a client connects to the server. Override to handle this event. Typical actions taken 
might be storing the new client in a list, sending an introductory message, or setting colors.

**on_receive**(*message*)

Override this method to receive messages from clients.

*message*: A string sent from the client.

**on_destroy**()

Called whenever a client is disconnected. Override to handle this event.

**destroy**()

Disconnect the client.

**write**(*string*, *color*=None)

Write a string to the terminal. Newline characters, '\n', result in a new line on the client terminal.

*string*: The string to write.

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**writeline**(*string*, *color*=None)

The same as Handler.write(), but appends a newline to the end.

**set_color**(color)

Sets the default text color in the output pane.

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**set_input_color**(*color*)

Sets the default text color in the input pane.

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**set_output_background_color**(*color*)

Sets the color of the output pane background.

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**set_input_background_color**(*color*)

Sets the color of the input pane background.

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**set_separator_color**(*color*)

Sets the color of the input/output sepatator line. 

*color*: A string representing the color to display the text in on the client. This can be anything 
the browser will understand as a color. Typical representations might be "red", "#FF0000", or 
"rgb(255,0,0)".

**set_password_mode**(*on*)

Makes the input field hide typed characters. Useful for authentication purposes.

*on*: True to hide typed characters, False to display them.
    

The Cellophane class
====================

class cellophane.Cellophane(client_class=Handler, hostname='localhost', 
                            port='8888', favicon_path=STATIC_PATH, 
                            title='cellophane', debug=True)
                            
    client_class: the class you have subclassed from Handler to handle your server-side logic
    hostname: this is the host name or ip address that the client will attempt to connect to via websockets
    port: the port the webpages are served and websockets are handled on
    favicon_path: if you want to override the built in favicon, point this to the path containing your favicon (not at the favicon itself)
    title: the page title for the web terminal
    debug: run Tornado in debug mode to see errors on the browser and automatically restart the server when code is changed        
    
    function periodic(function, time)
    
        This provides a means of running a function at a regular interval. This should be called before starting the server with Cellophane.go().
        
        function: the function to execute
        time: the amount of time, in milliseconds, between executions of function
        
    function go()
        
        Starts the web server and web socket server. This function blocks.

