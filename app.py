import json
#loading JSON files is JSon objects
with open('static\Source_data.json') as json_data:
    a = json.load(json_data,) 

with open('static\destination_data.json') as json_data:
    b = json.load(json_data,) 

out_source = {}
out_destination = {}

def flatten_source(x, name=''):
    
    if type(x) is dict:
        for a in x:
            flatten_source(x[a], name + a + '_')
    elif type(x) is list:
        i = 0
        for a in x:
            flatten_source(a, name + '[' + str(i) + ']_' )
            i += 1
    else:
        out_source[name[:-1]] = x

def flatten_destination(x, name=''):
    
    if type(x) is dict:
        for a in x:
            flatten_destination(x[a], name + a + '_')
    elif type(x) is list:
        i = 0
        for a in x:
            flatten_destination(a, name + '[' + str(i) + ']_' )
            i += 1
    else:
        out_destination[name[:-1]] = x

	

def differences(a, b, section = None):
  for [c, d], [h, g] in zip(a.items(), b.items()):
      if not isinstance(d, dict) and not isinstance(g, dict):
         if d != g:
            yield (d, g)
      else:
          for i in differences(d, g, c):
             for b in i:
               yield b

flatten_source(a)
flatten_destination(b)
x= (differences(out_source, out_destination)) 
for i in x:
	print i
