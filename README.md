The world's worst web server, implemented in [Pure Data](https://en.wikipedia.org/wiki/Pure_Data).

### tl;dr ###

 * Load up `web-server-help.pd` in Pd.
 * Visit http://aciles.mccormick.cx/
 * Send messages between Pd and your browser.

### What ###

Some things you could do with this:

 * Send messages from a web-app to Pd patches and visa versa.
 * Control a headless Raspberry Pi running Pd with a web-app on another machine.
 * Control a libpd patch running on a tablet or phone with a web-app in the devices's browser.

This is a hack and treats the HTTP protocol very roughly. Don't send too much data too fast either way.

### Web apps ###

To build a web-app that talks to Pd you can use the following code:

	<script src="http://aciles.mccormick.cx/aciles.js" type="text/javascript"></script>
	<script>
	  var server = "http://localhost:8999/"
	  aciles.send(server, "hello from the web-browser");
	  aciles.receiver(server,
	    function(data) { console.log("from Pd:", data); },
	    function(error) { console.log("error:", error); });
	</script>

Then in your patch instantiate the web-server:

	[web-server 8999 PD]

See the `web-server-help.pd` patch for more information on the Pd side.
