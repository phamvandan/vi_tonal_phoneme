## Run
### Example to encode a lst dir and save mapping table, which use for decode later
```
# create mapping table
python3 create_dict.py ./data/origin_lst ./data/output
python3 create_mapping.py ./data/output 
## word with spell errors will appear in error_dict.txt -> nor malize using
python3 nor_lst.py data/origin_lst data/nor_lst ./data/output
## recreate mapping table
python3 create_dict.py ./data/nor_lst ./data/output
python3 create_mapping.py ./data/output
## encode lst
python3 encode_lst.py ./data/nor_lst ./data/encoded_lst ./data/output
# decode sentence using mapping table
python3 decode_sentence.py ./data/output/mapping_table.txt
```
