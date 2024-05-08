import inspect
import  StudentAgentUploadsTemp
import  StudentAgentUploads
import sys



def make_player_list():
    from StudentAgentUploads.Group01Player import Group01Player
    from StudentAgentUploads.Group02Player import Group02Player
    from StudentAgentUploads.Group03Player import Group03Player
    from StudentAgentUploads.Group04Player import Group04Player
    from StudentAgentUploads.Group05Player import Group05Player
    from StudentAgentUploads.Group06Player import Group06Player
    from StudentAgentUploads.Group07Player import Group07Player
    from StudentAgentUploads.Group08Player import Group08Player
    from StudentAgentUploads.Group09Player import Group09Player
    from StudentAgentUploads.Group10Player import Group10Player
    from StudentAgentUploads.Group11Player import Group11Player
    from StudentAgentUploads.Group12Player import Group12Player
    from StudentAgentUploads.Group13Player import Group13Player
    from StudentAgentUploads.Group14Player import Group14Player
    from StudentAgentUploads.Group15Player import Group15Player
    from StudentAgentUploads.Group16Player import Group16Player
    from StudentAgentUploads.Group17Player import Group17Player
    from StudentAgentUploads.Group18Player import Group18Player
    from StudentAgentUploads.Group19Player import Group19Player
    from StudentAgentUploads.Group20Player import Group20Player
    from StudentAgentUploads.Group21Player import Group21Player
    from StudentAgentUploads.Group22Player import Group22Player
    from StudentAgentUploads.Group23Player import Group23Player
    from StudentAgentUploads.Group24Player import Group24Player
    from StudentAgentUploads.Group25Player import Group25Player
    from StudentAgentUploads.Group26Player import Group26Player
    from StudentAgentUploads.Group27Player import Group27Player
    from StudentAgentUploads.Group28Player import Group28Player
    from StudentAgentUploads.Group30Player import Group30Player
    from StudentAgentUploads.Group31Player import Group31Player
    from StudentAgentUploads.Group32Player import Group32Player
    from StudentAgentUploads.Group33Player import Group33Player
    from StudentAgentUploads.Group35Player import Group35Player
    from StudentAgentUploads.Group36Player import Group36Player
    from StudentAgentUploads.Group40Player import Group40Player
    from StudentAgentUploads.Group42Player import Group42Player
    from StudentAgentUploads.Group44Player import Group44Player
    from StudentAgentUploads.Group45Player import Group45Player
    from StudentAgentUploads.Group46Player import Group46Player
    from StudentAgentUploads.Group47Player import Group47Player
    from StudentAgentUploads.Group48Player import Group48Player
    from StudentAgentUploads.Group49Player import Group49Player
    from StudentAgentUploads.Group50Player import Group50Player

    player_list = []
    player_list.append(Group01Player())
    player_list.append(Group02Player())
    player_list.append(Group03Player())
    player_list.append(Group04Player())
    player_list.append(Group05Player())
    player_list.append(Group06Player())
    player_list.append(Group07Player())
    player_list.append(Group08Player())
    player_list.append(Group09Player())
    player_list.append(Group10Player())
    player_list.append(Group11Player())
    player_list.append(Group12Player())
    player_list.append(Group13Player())
    player_list.append(Group14Player())
    player_list.append(Group15Player())
    player_list.append(Group16Player())
    player_list.append(Group17Player())
    player_list.append(Group18Player())
    player_list.append(Group19Player())
    player_list.append(Group20Player())
    player_list.append(Group21Player())
    player_list.append(Group22Player())
    player_list.append(Group23Player())
    player_list.append(Group24Player())
    player_list.append(Group25Player())
    player_list.append(Group26Player())
    player_list.append(Group27Player())
    player_list.append(Group28Player())
    player_list.append(Group30Player())
    player_list.append(Group31Player())
    player_list.append(Group32Player())
    player_list.append(Group33Player())
    player_list.append(Group35Player())
    player_list.append(Group36Player())
    player_list.append(Group40Player())
    player_list.append(Group42Player())
    player_list.append(Group44Player())
    player_list.append(Group45Player())
    player_list.append(Group46Player())
    player_list.append(Group47Player())
    player_list.append(Group48Player())
    player_list.append(Group49Player())
    player_list.append(Group50Player())
    return player_list


def make_player_dict():
        reload(StudentAgentUploads)
        player_dict = {"Group01":  Group01Player(),
                        "Group02":  Group02Player(),
                        "Group03":  Group03Player(),
                        "Group04":  Group04Player(),
                        "Group05":  Group05Player(),
                        "Group06":  Group06Player(),
                        "Group07":  Group07Player(),
                        "Group08":  Group08Player(),
                        "Group09":  Group09Player(),
                        "Group10":  Group10Player(),
                        "Group11":  Group11Player(),
                        "Group12":  Group12Player(),
                        "Group13":  Group13Player(),
                        "Group14":  Group14Player(),
                        "Group15":  Group15Player(),
                        "Group16":  Group16Player(),
                        "Group17":  Group17Player(),
                        "Group18":  Group18Player(),
                        "Group19":  Group19Player(),
                        "Group20":  Group20Player(),
                        "Group21":  Group21Player(),
                        "Group22":  Group22Player(),
                        "Group23":  Group23Player(),
                        "Group24":  Group24Player(),
                        "Group25":  Group25Player(),
                        "Group26":  Group26Player(),
                        "Group27":  Group27Player(),
                        "Group28":  Group28Player(),
                        "Group30":  Group30Player(),
                        "Group31":  Group31Player(),
                        "Group32":  Group32Player(),
                        "Group33":  Group33Player(),
                        "Group35":  Group35Player(),
                        "Group36":  Group36Player(),
                        "Group40":  Group40Player(),
                        "Group42":  Group42Player(),
                        "Group44":  Group44Player(),
                        "Group45":  Group45Player(),
                        "Group46":  Group46Player(),
                        "Group47":  Group47Player(),
                        "Group48":  Group48Player(),
                        "Group49":  Group49Player(),
                        "Group50":  Group50Player()}
        return player_dict


def get_player(username):
    reload(StudentAgentUploadsTemp)
    if username == "Group01":
        from StudentAgentUploadsTemp.Group01Player import Group01Player as Group01
        return Group01()
    elif username == "Group02":
        from StudentAgentUploadsTemp.Group02Player import Group02Player as Group02
        return Group02()
    elif username == "Group03":
        from StudentAgentUploadsTemp.Group03Player import Group03Player as Group03
        return Group03()
    elif username == "Group04":
        from StudentAgentUploadsTemp.Group04Player import Group04Player as Group04
        return Group04()
    elif username == "Group05":
        from StudentAgentUploadsTemp.Group05Player import Group05Player as Group05
        return Group05()
    elif username == "Group06":
        from StudentAgentUploadsTemp.Group06Player import Group06Player as Group06
        return Group06()
    elif username == "Group07":
        from StudentAgentUploadsTemp.Group07Player import Group07Player as Group07
        return Group07()
    elif username == "Group08":
        from StudentAgentUploadsTemp.Group08Player import Group08Player as Group08
        return Group08()
    elif username == "Group09":
        from StudentAgentUploadsTemp.Group09Player import Group09Player as Group09
        return Group09()
    elif username == "Group10":
        from StudentAgentUploadsTemp.Group10Player import Group10Player as Group10
        return Group10()
    elif username == "Group11":
        from StudentAgentUploadsTemp.Group11Player import Group11Player as Group11
        return Group11()
    elif username == "Group12":
        from StudentAgentUploadsTemp.Group12Player import Group12Player as Group12
        return Group12()
    elif username == "Group13":
        from StudentAgentUploadsTemp.Group13Player import Group13Player as Group13
        return Group13()
    elif username == "Group14":
        from StudentAgentUploadsTemp.Group14Player import Group14Player as Group14
        return Group14()
    elif username == "Group15":
        from StudentAgentUploadsTemp.Group15Player import Group15Player as Group15
        return Group15()
    elif username == "Group16":
        from StudentAgentUploadsTemp.Group16Player import Group16Player as Group16
        return Group16()
    elif username == "Group17":
        from StudentAgentUploadsTemp.Group17Player import Group17Player as Group17
        return Group17()
    elif username == "Group18":
        from StudentAgentUploadsTemp.Group18Player import Group18Player as Group18
        return Group18()
    elif username == "Group19":
        from StudentAgentUploadsTemp.Group19Player import Group19Player as Group19
        return Group19()
    elif username == "Group20":
        from StudentAgentUploadsTemp.Group20Player import Group20Player as Group20
        return Group20()
    elif username == "Group21":
        from StudentAgentUploadsTemp.Group21Player import Group21Player as Group21
        return Group21()
    elif username == "Group22":
        from StudentAgentUploadsTemp.Group22Player import Group22Player as Group22
        return Group22()
    elif username == "Group23":
        from StudentAgentUploadsTemp.Group23Player import Group23Player as Group23
        return Group23()
    elif username == "Group24":
        from StudentAgentUploadsTemp.Group24Player import Group24Player as Group24
        return Group24()
    elif username == "Group25":
        from StudentAgentUploadsTemp.Group25Player import Group25Player as Group25
        return Group25()
    elif username == "Group26":
        from StudentAgentUploadsTemp.Group26Player import Group26Player as Group26
        return Group26()
    elif username == "Group27":
        from StudentAgentUploadsTemp.Group27Player import Group27Player as Group27
        return Group27()
    elif username == "Group28":
        from StudentAgentUploadsTemp.Group28Player import Group28Player as Group28
        return Group28()
    elif username == "Group30":
        from StudentAgentUploadsTemp.Group30Player import Group30Player as Group30
        return Group30()
    elif username == "Group31":
        from StudentAgentUploadsTemp.Group31Player import Group31Player as Group31
        return Group31()
    elif username == "Group32":
        from StudentAgentUploadsTemp.Group32Player import Group32Player as Group32
        return Group32()
    elif username == "Group33":
        from StudentAgentUploadsTemp.Group33Player import Group33Player as Group33
        return Group33()
    elif username == "Group35":
        from StudentAgentUploadsTemp.Group35Player import Group35Player as Group35
        return Group35()
    elif username == "Group36":
        from StudentAgentUploadsTemp.Group36Player import Group36Player as Group36
        return Group36()
    elif username == "Group40":
        from StudentAgentUploadsTemp.Group40Player import Group40Player as Group40
        return Group40()
    elif username == "Group42":
        from StudentAgentUploadsTemp.Group42Player import Group42Player as Group42
        return Group42()
    elif username == "Group44":
        from StudentAgentUploadsTemp.Group44Player import Group44Player as Group44
        return Group44()
    elif username == "Group45":
        from StudentAgentUploadsTemp.Group45Player import Group45Player as Group45
        return Group45()
    elif username == "Group46":
        from StudentAgentUploadsTemp.Group46Player import Group46Player as Group46
        return Group46()
    elif username == "Group47":
        from StudentAgentUploadsTemp.Group47Player import Group47Player as Group47
        return Group47()
    elif username == "Group48":
        from StudentAgentUploadsTemp.Group48Player import Group48Player as Group48
        return Group48()
    elif username == "Group49":
        from StudentAgentUploadsTemp.Group49Player import Group49Player as Group49
        return Group49()
    elif username == "Group50":
        from StudentAgentUploadsTemp.Group50Player import Group50Player as Group50
        return Group50()