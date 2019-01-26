# Resources

This folder contains whitepapers, APT reports, and etc used for this research

## PDF extractor

This Python tool will create a list of PDFs that contain defined keywords.

1. `cd pdf_extractor`
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`
1. `python3 pdf_extractor.py --path <path> --keyword <keyword>`
    1. Example: `python3 pdf_extractor.py --path /tmp/APT_CyberCriminal_Campagin_Collections --keyword 'lateral movement'`
        1. Path: `/tmp/APT_CyberCriminal_Campagin_Collections`
        1. Keyword: `lateral movement`
1. An output file of `<keyword>.txt` will be generated with a list of PDFs that contain that keyword.

## APT reports

* [Github - kbandla/APTnotes](https://github.com/kbandla/APTnotes)
* [Github - aptnotes/data](https://github.com/aptnotes/data)
* [Github - CyberMonitor/APT_CyberCriminal_Campagin_Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)

## Whitepapers

## Blog posts

## Resources/Sources

* [Python, argparse, and command line arguments](https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/)
* [Recursive sub folder search and return files in a list python](https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python)
* [How to Extract Words from PDFs with Python](https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f)
