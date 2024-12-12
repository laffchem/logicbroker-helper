# Logicbroker Helper

If you have python installed you're good to go.

## Installation Instructions

**In the terminal, ensure you're in the directory and then this will explain how to install the program**

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### How to use

Inside the src folder, paste in the values you need into input-values.txt

When Risk asks you to hold a bunch of orders, you have either the calypso links or the ids.

Paste their request into the "risk-values.txt" file as is.

Run the program and select the values.

Calypso links
ID Values

Select if you need a hold or release query.

**Then after the program runs, the query is generated to output.txt.**

_Underneath the query to hold or release is the SELECT query so you can check if there are any that were already submitted_

You can paste that into mysql and make this a little more simple.
