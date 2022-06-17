# shasha-cloud-api

Welcome to the documentation of **shashacloud.**

# THE CURRENT VERSION IS OUTDATED, THE NEW VERSION WILL RELEASE AFTER SOME TIME. CREATE AN ISSUE FOR MORE INFORMATION.

Here are the list of commands:
`login` (IMPORTANT),
`send_file`,
`get_link`,
`search_file`,
`get_file`,
`download`,
`rename_file`

Usage:

login: (This login function has to be run before every other function)
```py
import shashacloud

shashacloud.login(username, password)
```

send_file: sends a file
```py
import shashacloud

shashacloud.login(username, password)
shashacloud.send_file("Files\\MyFiles\\Sample.txt")
```

get_link:
```py
import shashacloud

shashacloud.login(username, password)
shashacloud.get_link(filename)
```

search_file: searches for a file in the storage
```py
import shashacloud

shashacloud.login(username, password)
var = shashacloud.search_file(filename)
print(var)
```

get_files: lists all the files in the storage
```py
import shashacloud

shashacloud.login(username, password)
var = shashacloud.get_files()
print(var)
```

download: downloads a file into a particular directory
```py
import shashacloud

shashacloud.login(username, password)
shashacloud.download('Sample.txt',your_directory)
```

rename_file:
```py
import shashacloud

shashacloud.login(username, password)
shashacloud.rename_file('Sample.txt','NewSample.txt')
```
