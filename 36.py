
import json
from collections import Counter

with open("birthdays.json", "r") as f:
	birthdays = json.load(f)

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []
for name, birthday_string in birthdays.items():
	month = int(birthday_string.split("/")[0])
	months.append(num_to_string[month])

# print(Counter(months))
a = list(Counter(months).elements())

d = {}

for words in a:
    if words in d:
	    d[words] += 1
    else:
	    d[words] = 1


from bokeh.plotting import figure, show, output_file

# we specify an HTML file where the output will go
output_file("plot.html")

# load our x and y data
x = d.keys()
y = d.values()

print x,y 
p = figure()

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)
