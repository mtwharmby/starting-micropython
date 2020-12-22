import machine

import picoweb
from net import get_ipaddress, is_connected


# Configure the LED. N.B. Pin D5!
pin = machine.Pin(5, machine.Pin.OUT)
pin.off()


# Create an instance of the picoweb webserver app
print("Configuring web server...")
app = picoweb.WebApp("__main__")


@app.route("/")
def index(req, resp):
    # The root page of the website - the ledcontol page
    print(req)
    yield from app.sendfile(resp, "html/ledControl.html",
                            content_type="text/html")


@app.route("/ledOn")
def led_on(req, resp):
    # Switch LED on and returned the LED control page, when the "LED On" button
    # is clicked
    pin.on()
    print("LED switched on...")
    yield from app.sendfile(resp, "html/ledControl.html",
                            content_type="text/html")


@app.route("/ledOff")
def led_off(req, resp):
    # Switch LED off and returned the LED control page, when the "LED On"
    # button is clicked
    pin.off()
    print("LED switched off...")
    yield from app.sendfile(resp, "html/ledControl.html",
                            content_type="text/html")


# If we're connected to a network, start picoweb. If <Ctrl>+C is pressed, kill
# the app and hide the stacktrace
if is_connected():
    try:
        print("Running webserver...")
        app.run(debug=True, host=get_ipaddress())
    except KeyboardInterrupt:
        print("Stopping server...")
else:
    print("No network connection. Not starting the webserver.")
