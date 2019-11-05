# List of useful VIM commands

 * cut(d), yank(y), change(c) from cursor untill X character:
 
   `ytX` e.g. |obj["prop"] -> `yt]` will copy obj["prop"] into the buffer
   
              ^cursor
              
   If there are multiple X characters before the target character use VIM command multipliers
   `3ytX` e.g. |obj["propA"]["propB"]["propC"] -> `3yt]` will copy obj["propA"]["propB"]["propC"]
   
   
 * In order to avoid deleting(d) into any buffer and keep the `p` command clean, prefix the command with `"_`. The `"` character 
 essentially tells VIM that anything that will be put into a buffer must be put into the buffer represented by the character that
 follows it. The `_` character is special in that it represents "no buffer" which means that whetever is deleted(d) will be thrown
 away and will keep `p` buffer clean.
