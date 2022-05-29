# dj-crudo
Replacing a google form with this crud... Because I'm a simple man with simple needs...

**Not ready for production!!!**
__superuser is created programatically at startup using admin/pass credentials... yes i know...__

This project uses **pipe** to comunicate with the host through the included pipe_line.sh script.
A pipe must be created at (root)/pipe in the local host to receive commands from the docker... what can possible go wrong with it... The point of this is allowing IPTABLES to be handled by this app... Again, what can possile goes wrong, right? RIGHT?

(btw: I'm using 'chown $USER:$USER /pipe' and 'chmod 600 /pipe')
