# ghfetch
ghfetch is ai customizable CLI GitHub personal README generator. Inspired by famous fetch such as
screenfetch, neofetch and ufetch, the purpose of this tool is to introduce yourself as if you were a machine.

## Setup
Edit `src/config.ini` with your personal informations, such as age, programming languages, etc. By default there are two sections: main and contacts, but it's possible add others.

## Usage
Run this command and it will be created your README
```
$ ./main.py
             %&M#*oooo*#M&%               hostname@country
         %MakbbbbbbbbbbbbbbkaM%           ----------------
      BMhbbbbbbbbbbbbbbbbbbbbbbhMB        Uptime: "18 years"
    @*kbbbbbbbbbbbbbbbbbbbbbbbbbbk*@      Programming Languages: ""
   &kbbbbM&Mokbbbbbbbbbbbbk*M&Mbbbbk&     OS: ""
  #bbbbbh     %8%B@@@@B%8%     hbbbbb#    Editor: ""
 Mbbbbbbk                      kbbbbbbM   Hobbies: ""
%kbbbbbkM                      Mkbbbbbk%
*bbbbbb#                        #bbbbbb*  Contacts
kbbbbbb%                        %bbbbbbk  --------
kbbbbbb8                        8bbbbbbk  Email: ""
abbbbbb*                        *bbbbbba
WbbbbbbkW                      WkbbbbbbW
 hbbbbbbbo8                  8obbbbbbbh
 Bkbbo%8*kbko#W&        &W#okbbbbbbbbkB
  BabbkM 8hbbbb8        8bbbbbbbbbbbaB
    Mkbb#  B%%@          bbbbbbbbbkM
     B#kbk*#MMM          bbbbbbbk#B
       @Wokbbbb          bbbbkoW@
           8M**          **M8
```

The default logo is GitHub, but you can choose from several other logos
```
$ ./main.py --logo gitlab
      %+%                      %+%        hostname@country
      +++                      +++        ----------------
     #+++#                    #+++*       Uptime: "18 years"
    %+++++%                  %+++++%      Programming Languages: ""
    *+++++*                  *++++++      OS: ""
   #+++++++#                #+++++++#     Editor: ""
  %+++++++++%              %+++++++++%    Hobbies: ""
  ===========**************===========
 *---=========++++++++++++=========---+   Contacts
%-----========++++++++++++========-----%  --------
=-------=======++++++++++=======-------=  Email: ""
#+--------======+++++++++======-------=#
   *=------=====++++++++=====------=*
     %*------====++++++====------*%
        %+----===++++++===----+%
           #+---==++++==---=#
              *=-==++==-=*
                %*=++=*%
```

You can also create your own ascii logo and use it
```
$ ./main.py --generate_ascii path/to/image
$ ./main.py --logo custom
            ```                             cele@italy
          `,,`      ,;cc;`                  ----------
        `;;,`     `l0NWWKl`                 Uptime; "18 years"
      `;c;,      `oXMMMMMXd,                Languages; "Python, C++"
     ,;c;,      ,dNMMMMMMMNx,               OS; "Arch Linux"
   `,clc,      ;xNMMWXOONMMWk;              DE; "KDE Plasma"
  `;cll;`     ;0WMMNxc,,dNMMWO;`            Shell; "Zsh"
  ;clll;`   `;0WMMNd,   `oXMMW0c`           Editor; "Vim, VSCode"
 ,cllll;`  `cKMMMXo`     `lKMMMKc`          Hobbies; "hip hop, football, gaming"
`;lllll;` `lXMMMKl`       `cKMMMKc`   ```   Other; "2021 OII finalist (Olimpiadi Italiane di Informatica)"
`;llllll;`;0WMW0c`         `cKWWNx, ,;;,
`;llloool;;cx0k;            `;doc;;;;;`
`;llooooool;;;,            `,;;cllc;,`
 ,clooooooooolcc;;;;;;;;;cllodoc;;lk0o`     contacts
  ,;looooooooddddddddddddddlc;, ,xNMMXo`    --------
   `,;clooodddddddddoolc;;,`     ;0WMMXl`   Telegram; "t.me/nastybox"
      `,;;;;;;;;;;;,,``           ;xXXOc    Reddit; "u/alessiocelentano"
                                   `,;,     Email; "alessiocelentano2003@gmail.com"

```

## Credits
[ASCII generator](https://github.com/uvipen/ASCII-generator)
