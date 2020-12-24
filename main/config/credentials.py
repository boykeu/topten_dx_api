from ..main_fun.func import fernie

KEY               = b'=YZONueEnD9Rno1gSo0zdFBeqhuwyNy4wzBHcy3wuDye'

DB_CONN = \
  {
  "conn": [
      {
        "host"     : fernie(b'gAAAAABf4h1wREaYMJRtCQfrFnL89GtFgW78tCPTzaLdWO8rq4wJ5UR9_I1Pe_sQgwv2JTRM9CO9qPUvtmZX-dshRmk91QJe3g==',KEY[::-1]),
        "database" : fernie(b'gAAAAABf4h6hUxiO9dHeglPOn9NXssHdU1rPEESZ1M75uNvz4UFdwcajjQYiC69T3dKbr3i0IJVZ2BphPLFiJO3A1VY9Eil2vg==',KEY[::-1]),
        "user"     : fernie(b'gAAAAABf4iiURO3LZvzyJn68PJZClnn4xZ9y7XFF2wEiNcvRC1RbmY_oP0qJ_kOpA7wN3EyR8DZADb3V4W9Q27RoLdqbkl1txg==',KEY[::-1]),
        "password" : fernie(b'gAAAAABf4iiURO3LZvzyJn68PJZClnn4xZ9y7XFF2wEiNcvRC1RbmY_oP0qJ_kOpA7wN3EyR8DZADb3V4W9Q27RoLdqbkl1txg==',KEY[::-1])
      } 
    ]
  }