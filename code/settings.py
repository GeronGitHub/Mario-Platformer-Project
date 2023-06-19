import pygame

level_map = [

    '                      V                WW                              X',
    '                                          D                            X',
    '                           D         D                                 X',
    '                      G         D                                      X',
    '                    WWWW                                               X',
    '                             D                                         X',
    '                  GDD  DD                     B                        X',
    '                 DDXX  XXDD          WWWW  B          B                X',
    '         B      DXXXX  XXXXD    B    BBBB         B          V         X',
    '               DXXXXX  XXXXXD                                          X',
    '     P   G  T DXXXXXX  XXXXXXD   T   G   G   T G      TT               X',
    'DDDDDDDDDDDDDDXXXXXXX  XXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDX'
]

level_map2 = [

    '                                                                       X',
    '                       W            W                                  X',
    '                  WW   B            BB W                               X',
    '                  B      WW          BB WW                             X',
    '              W       B  BB             BB                        V    X',
    '              B                B     BB                                X',
    '                 B           B                   G       B  B   BB     X',
    '               B   B   B         B        B  B  B        B             X',
    '             B                      B        B  B                      X',
    '           B  XX          XX                      BBB                 X',
    'X    P XXX  G    XX       XX                      XXX                 XX',
    'DDDDDDDDDDDDDDXXXXX       XX            DDDD           XDD   XXX      XX'
]


tile_size = 50

screen_width = 1000
screen_height = 640  # len(level_map) * tile_size #500
FPS = 60


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ULTRA MARIO BROS.')
