import pygame, os, sys, requests, random
        
pygame.init()       # Margin all sides 30px

# Constant
win_Size = (1280, 680)
fps = 60
black_Text = (0,0,0)
surf_Bg = (255, 255, 255, 220)
blue_Bg = (135, 206, 235, 240)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Utilitiy Functions

def event_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit; sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
                
            for f in form_layout["login_fields"]:
                
                if f["rect"] and f["rect"].collidepoint(mouse_pos):    
                    f["active"] = True
                else:
                    f["active"] = False
            
            if form_layout["status"]["login_active"] and form_layout["login_btn"][1].collidepoint(mouse_pos):
                input_validation()

                
            for f in form_layout["int_fields"]["fields"]:

                if form_layout["run"] and f["rect"].collidepoint(mouse_pos):
                    
                    form_layout["int_fields"]["user_input"].append(f["lable"])
                    f["active"] = True
                if len(form_layout["int_fields"]["user_input"]) >= 3 and form_layout["int_fields"]["button"].collidepoint(mouse_pos):
                    
                    form_layout["run"] = False
                
            # if form_layout["int_fields"]["button"].collidepoint(mouse_pos):
            #     user_data()
                
                
        if event.type == pygame.KEYDOWN:      
            for f in form_layout["login_fields"]:
                if f["active"]:
                    if event.key == pygame.K_BACKSPACE:
                        f["text"] = f["text"][:-1]
                    elif event.key == pygame.K_RETURN:
                        f["active"] = False
                    else:
                        f["text"] += event.unicode
                           
def asset_path(*path_parts):
    """Return absolute path for any asset (font, image, etc.)"""
    return os.path.join(BASE_DIR, *path_parts)

def load_font(wgt: str, size: int):
    valid_weight = ["Thin","Light","ExtraLight","Regular","Medium","SemiBold","Bold","ExtraBold","Black"]
    if wgt not in valid_weight:
        wgt = "Regular"
    
    full_path = asset_path(f"Poppins/Poppins-{wgt}.ttf")
    try:
        return pygame.font.Font(full_path, size)
    except pygame.error:
        print(f"Error loading {wgt}. Trying Regular...")
        return pygame.font.Font(asset_path('Poppins/Poppins-Regular.ttf'), size)
    
def input_validation():

    if form_layout["login_fields"][0]["text"] == "Admin" and form_layout["login_fields"][1]["text"] == "12345678":
        form_layout["running"] = True
        form_layout["status"]["user_cred"] = False
 
    else:
        form_layout["invalid"] = True

def user_interest(form_layout):
    event_check()

    int_surf = pygame.Surface(win_Size,pygame.SRCALPHA)
    int_surf.fill((0,0,0, 230))
    
    form_layout["int_fields"]["main_rect"].center = (win.get_width() // 2, win.get_height() // 2)
    pygame.draw.rect(int_surf, (217, 217, 217),form_layout["int_fields"]["main_rect"],border_radius=30)

    title = load_font("Regular", 32).render(form_layout["int_fields"]["title"], True, (0, 0, 0),(217, 217, 217))
    title_rect = title.get_rect(topleft=(444, 80))
    
    pygame.draw.line(int_surf,(50, 50, 50), (340,130),(940,130 ), 2)
    for f , lst in enumerate(form_layout["int_fields"]["fields"]):
        
        box_color =  (255, 0, 0 ) if lst["active"] else (83, 162, 218)
        pygame.draw.rect(int_surf, box_color,lst["rect"], border_radius=30)
        center_x , center_y = lst["rect"][0] , lst["rect"][1]
        interest = load_font("Medium", 16).render(lst["lable"], True, (255, 255, 255))
        interest_rect = interest.get_rect(center=(center_x + 128, center_y + 25))
        
        form_layout["int_fields"]["button"] = pygame.draw.rect(int_surf,(50, 255,50), (370, 547, 540, 55), border_radius=15)
        button_x , button_y = form_layout["int_fields"]["button"][0], form_layout["int_fields"]["button"][1]
        submit = load_font("Medium",24).render("Continue", True, black_Text, (50, 255,50))
        submit_rect = submit.get_rect(center=(button_x + 270, button_y + 26))


        int_surf.blits([(interest, interest_rect),(submit, submit_rect)])
    
  
    int_surf.blit(title, title_rect)
    win.blit(int_surf, (0,0))

    pygame.display.update()
    clock.tick(fps)
        
    
def load_image(name, size):
    img = pygame.image.load(asset_path(name)).convert_alpha()
    return pygame.transform.smoothscale(img, size) if size else img


def animation():
    
    duration = 8000
    start_time = pygame.time.get_ticks()
    
    while pygame.time.get_ticks() - start_time < duration:
        # game_event()
        
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit; sys.exit()
            
        
        elapsed = (pygame.time.get_ticks() - start_time) / duration
        alpha = max(0, min(255, int(elapsed * 255)))
        
        img = load_image("logo.png",(70, 70))
        img_rect = img.get_rect(center=(win.get_width() // 2, win.get_height() // 2 - 35))
        img.set_alpha(alpha)
        
        brand = load_font("Regular", 24).render("Arctic Fox Gamers", True, (alpha, alpha, alpha))
        brand_rect = brand.get_rect(center=(win.get_width() // 2, win.get_height() // 2 + 35))

        blit_sequence = [(brand, brand_rect),(img, img_rect)]
       
        win.fill((0, 0, 0))
        win.blits(blit_sequence)
        
        pygame.display.flip()
        clock.tick(fps)
    

def form_page(surface):
    
    while form_layout["status"]["user_cred"]:
        event_check()
        
        surface.fill((200, 200, 200))
        img_logo = load_image("millionaire.png",(250,250))
        
        title = load_font("SemiBold", 40).render("The Ultimate Brain Test", True, black_Text, (200, 200, 200))

        quote = [('"The will to win, the desire to succeed, the urge'), ("to reach your full potential... these are the keys"), ('that will unlock the door to personal excellence."')]

        for i , line in enumerate(quote):
            quote_render = load_font("Regular", 18).render(line , True, (75, 75, 75), (200, 200, 200))
            quote_rect = quote_render.get_rect(topleft=(130, 440 + (25 * i)))
            
            surface.blit(quote_render, quote_rect)
            
        pygame.draw.line(surface,(50, 50, 50), (670,155),(670,475 ), 2)

        # form page register

        
        if form_layout["status"]["register_active"]:
            
            pygame.draw.rect(surface,(100, 100, 100),(surface.get_width() - 520, 80 ,450, 460),border_radius=20)
            
            title_form = load_font("Regular", 32).render(form_layout["title"][0], True, black_Text,(233, 233, 233))
            title_rect = title_form.get_rect(midtop=(surface.get_width() - 295, 100))
            
            
            for i ,lst in enumerate(form_layout["fields"]):
                
                lable = load_font("Regular", 18).render(f'{lst["lable"]}', True, black_Text, (233, 233, 233))
                lable_rect = lable.get_rect(topleft=(800, 190 + (i * 55)))
                
                box_color = (180, 220, 255) if lst["active"] else (255, 255, 255)
                pygame.draw.rect(surface, box_color, lst["rect"], border_radius=12)
                
                input_text =load_font("Regular", 16).render(f"{lst["text"]}", True, black_Text)
                input_rect = input_text.get_rect(topleft=(920, 191 + (i * 55)))
            
                surface.blits([(lable, lable_rect),(input_text,input_rect)])
                
            pygame.draw.rect(surface,(135, 200, 255),(885, 420, 220, 50),border_radius= 14)

            
            button = load_font("Meduim", 24).render("Submit", True, black_Text, (135, 200, 255))
            button_rect = button.get_rect(midtop=(995 ,428))

            
            have_account = load_font("Regular", 16).render("Already have an account? Log In", True, (35, 35, 35), (233, 233, 233))
            form_layout["swap_rect"] = have_account.get_rect(midbottom=(995,520))
            
                
        elif  form_layout["status"]["login_active"]:
            
            pygame.draw.rect(surface,(220, 220, 220),(surface.get_width() - 520, 130 ,450, 360),border_radius=20)
            
            title_form = load_font("Regular", 32).render(form_layout["title"][1], True, black_Text,(220, 220, 220))
            title_rect = title_form.get_rect(midtop=(surface.get_width() - 295, 160))
            
            for i ,lst in enumerate(form_layout["login_fields"]):
                lable = load_font("Regular", 18).render(f'{lst["lable"]}', True, black_Text, (220, 220, 220))
                lable_rect = lable.get_rect(topleft=(800, 260 + (i * 55)))
                
                box_color = (180, 220, 255) if lst["active"] else (255, 255, 255)
                pygame.draw.rect(surface, box_color, lst["rect"], border_radius=12)
                
                input_text =load_font("Regular", 16).render(f"{lst["text"]}", True, black_Text)
                input_rect = input_text.get_rect(topleft=(920, 263 + (i * 55)))
                
                surface.blits([(lable, lable_rect),(input_text,input_rect)])
            
            form_layout["login_btn"][1] =pygame.draw.rect(surface,(135, 200, 255),(885, 386, 220, 50),border_radius= 14)
            
            button = load_font("Meduim", 24).render(form_layout["login_btn"][0], True, black_Text, (135, 200, 255))
            button_rect = button.get_rect(midbottom=(995 ,428))
            
            # have_account = load_font("Regular", 16).render("Note:_", True, (35, 35, 35), (233, 233, 233))
            # form_layout["swap_rect"] = have_account.get_rect(midtop=(995,450))
            
            # Temporary Notice: when remove this code uncomment upper line code ^
            notice = load_font("SemiBold", 24).render("Note:", True, (35, 35, 35), (200, 200, 200))
            notice_rect  = notice.get_rect(midtop=(800,550))
            
            email_id = load_font("Medium", 18).render("Email:  Admin", True, (255, 0, 0), (200, 200, 200))
            email_rect = email_id.get_rect(topleft=(850, 555))
            
            passcode = load_font("Medium", 18).render("Password:  12345678", True, (255, 0, 0), (200, 200, 200))
            passcode_rect = passcode.get_rect(topleft=(850, 585))
            
            if form_layout["invalid"]:
                invalid = load_font("Regular", 16).render("Invalid Username or Password", True, (255, 0, 0), (220, 220, 220))
                invalid_rect = passcode.get_rect(topleft=(850, 215))
                surface.blit(invalid, invalid_rect)
                
            surface.blits([(notice, notice_rect),(email_id, email_rect),(passcode, passcode_rect)])

 
                
        surface.blits([(img_logo, (220, 100)),(title, (105, 370)),(title_form,title_rect),(button, button_rect),(input_text, input_rect)])
        
        pygame.display.update()
        clock.tick(fps)


    
#Setup
win = pygame.display.set_mode(win_Size)
pygame.display.set_caption("Millionaire")
clock = pygame.time.Clock()

main_bg = pygame.transform.scale(pygame.image.load(asset_path('pic4.jpg')).convert_alpha(),win.get_size())
main_Surf = pygame.Surface(win_Size,pygame.SRCALPHA)
main_surf_rect = main_Surf.get_rect()

# Interest Choice
form_layout = {
    "title" : ["Register", "Login"],
    "status": {"register_active": False,
               "login_active" : True,
               "user_cred" : True},
    "swap_rect" : pygame.Rect(0, 0, 0, 0),
    "fields" : [
            {"lable" : "Fullname:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 183, 280, 40), "active" : False, "error" : None
        },
            {"lable" : "Age:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 238, 280, 40), "active" : False, "error" : None
        },
            {"lable" : "Email:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 293, 280, 40), "active" : False, "error" : None
        },
            {"lable" : "Password:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 348, 280, 40), "active" : False, "error" : None
        } 
    ],
    "login_fields" :  [
            {"lable" : "Username:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 255, 280, 40), "active" : False, "error" : None
        },
            {"lable" : "Password:","text" : "", "validation" : "string", "password" : False, "rect" : pygame.Rect(905, 310, 280, 40), "active" : False, "error" : None
        }
    ],
    "login_btn" : ["Login",pygame.Rect(0, 0, 0, 0)],
    "invalid" : False,
    "running" : True,
    "run" : True,
    "int_fields" : {
        "main_rect" : pygame.Rect(0, 0, 600, 540),
        "title" : "Choose Atleast 3 interest",
        "user_input" :  ["book & author"],
        "button" : pygame.Rect(0, 0, 540, 55), 
        "fields" : [
            {"lable" : "Technology & Programming", "active" : False, "rect" : pygame.Rect(370, 155,255, 52)},
            {"lable" : "Gaming & Game Dev", "active" : False, "rect" : pygame.Rect(370, 221,255, 52)},
            {"lable" : "Art & Design", "active" : False, "rect" : pygame.Rect(370, 287,255, 52)},
            {"lable" : "Music & Audio Production", "active" : False, "rect" : pygame.Rect(370, 353,255, 52)},
            {"lable" : "Travel & Adventure", "active" : False, "rect" : pygame.Rect(370, 419,255, 52)},
            {"lable" : "Fitness & Health", "active" : False, "rect" : pygame.Rect(370, 485,255, 52)},
            {"lable" : "Books & Author", "active" : False, "rect" : pygame.Rect(655, 155,255, 52)},
            {"lable" : "Movies & Series", "active" : False, "rect" : pygame.Rect(655, 221,255, 52)},
            {"lable" : "Cooking & Food Exploraion", "active" : False, "rect" :pygame.Rect(655, 287,255, 52)},
            {"lable" : "Business & Entrepreneurship", "active" : False, "rect" : pygame.Rect(655, 353,255, 52)},
            {"lable" : "News & Sports", "active" : False, "rect" : pygame.Rect(655, 419,255, 52)},
            {"lable" : "Politics", "active" : False, "rect" : pygame.Rect(655, 485,255, 52)},
                    ] }
   
}

main_asset = {
    "title" : "Millionaire",
    "leaderboard" :{
        "title" : "Leaderboard",
        "price_amount" : ["7,00,00,000", "1,00,00,000", "50,00,000", "25,00,000", "12,50,000", "6,40,000", "3,20,000", "1,60,000", "80,000", "40,000", "20,000", "10,000", "5000", "3000", "2000", "1000"],
        "price_box_rect" : pygame.Rect(950, 115, 300, 545)},
    "timer" : {
        "circle_pos" :  (483, 165),
        "circle_radius" : 50,
    },
    "ques_box" : {
        "box_rect" : pygame.Rect(30, 230, 900, 120),
        "lable" : '"Press START button to play the game.."'
    },
    "option" : {
        "fields" : [
                    {"lable" :"A:", "rect" : pygame.Rect(35,375, 425, 60), "active" : False},
                    {"lable" :"B:", "rect" : pygame.Rect(495, 375, 425, 60), "active" : False},
                    {"lable" :"C:", "rect" : pygame.Rect(35, 450, 425, 60), "active" : False},
                    {"lable" :"D:", "rect" : pygame.Rect(495, 450, 425, 60), "active" : False}] 
                },
    "buttons" : {
        "box" : pygame.Rect(30 , 540 , 900, 120),
        "images" : ["remove.png","call.png","swap.png","election.png","fifty.png", "start-button.png"]
    }
            }


def main_game():
     
    while form_layout["running"]:
        event_check()
        
        # Main Title
        main_Title_Surf = load_font("SemiBold", 50).render(main_asset["title"], True, black_Text)
        main_Title_Rect = main_Title_Surf.get_rect(midtop=(win_Size[0] // 2, 10))
        

        # Winning Amount
        
        pygame.draw.rect(main_Surf,surf_Bg,main_asset["leaderboard"]["price_box_rect"], border_radius=20)
        price_title_Surf = load_font("Regular", 32).render(main_asset["leaderboard"]["title"], True, black_Text)
        price_title_Rect = price_title_Surf.get_rect(midtop=(1100, 120))
        pygame.draw.line(main_Surf,(125, 125, 125), (950 ,165), (1250, 165), 1)

        for i, amount in enumerate(main_asset["leaderboard"]["price_amount"]):

            price_Text = load_font("Regular", 16).render(f"{16 - i}.  {amount}", True, black_Text)
            price_Score_Rect = price_Text.get_rect(topleft=(1030, 175 + (i * 30)))
            main_Surf.blit(price_Text, price_Score_Rect)

        # Timer
       
        pygame.draw.circle(main_Surf, surf_Bg, main_asset["timer"]["circle_pos"] , main_asset["timer"]["circle_radius"])
        timer_Surf = load_font("SemiBold", 40).render("60", True, black_Text)
        timer_Rect = timer_Surf.get_rect(center= main_asset["timer"]["circle_pos"])

        # Question Field
        ques_Box = pygame.draw.rect(main_Surf,surf_Bg,main_asset["ques_box"]["box_rect"], border_radius= 100)
        ques_Surf = load_font("Regular", 20).render(main_asset["ques_box"]["lable"], True, black_Text)
        ques_text_Rect = ques_Surf.get_rect(center=(ques_Box.center))

        # Options

        for i ,lable in enumerate(main_asset["option"]["fields"]):

            box = pygame.draw.rect(main_Surf, surf_Bg, lable["rect"], border_radius=16)
            lable = load_font("Medium", 24).render(lable["lable"], True, black_Text)
            lable_rect = lable.get_rect(midleft=(box.x + 15, box.y + 30))
            main_Surf.blit(lable, lable_rect)

        # Life-line  
        ll_rect = pygame.draw.rect(main_Surf,surf_Bg,main_asset["buttons"]["box"], border_radius= 100)

        for i ,name in enumerate(main_asset["buttons"]["images"]):
            img = load_image(asset_path(name), (70 ,70))
            img_Rect = img.get_rect(midleft=(125 * (1 + i) , ll_rect.centery))
            main_Surf.blit(img , img_Rect)

        main_Surf.blits([(main_Title_Surf, (main_Title_Rect)),(price_title_Surf, price_title_Rect),(timer_Surf,timer_Rect),(ques_Surf,ques_text_Rect)])

        # Main loop

        win.blit(main_bg, (0,0))
        win.blit(main_Surf, (0,0))
        
        if form_layout["run"]:
            user_interest(form_layout)
        pygame.display.update()
        clock.tick(fps)

animation()
form_page(win)
main_game()