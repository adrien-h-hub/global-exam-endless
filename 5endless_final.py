"""
5ENDLESS FINAL TEST VERSION - NO PAUSE (Standalone Repo)
"""
import time
import os
import getpass
import pyautogui
# Import your helper functions (final_test.py must be in the same folder)
from final_test import click_button as _click_button, answer_multi_blank, click_image

# Small safety delay after each click to avoid skipping questions on slow pages
def click_button(delay: float = 0.8):
    _click_button()
    time.sleep(delay)

# One-time hidden code check (stored via a marker file in the project folder)
def ensure_first_run_auth(code_value: str = "602172", marker_file: str = ".first_run_ok"):
    try:
        if os.path.exists(marker_file):
            return
        for attempt in range(3):
            user_input = getpass.getpass("Enter one-time code: ")
            if user_input.strip() == code_value:
                with open(marker_file, "w", encoding="utf-8") as f:
                    f.write("ok\n")
                return
            print("Incorrect code. Try again.")
        raise SystemExit("Too many failed attempts. Exiting.")
    except KeyboardInterrupt:
        raise SystemExit("\nCancelled by user.")

def run_final_once():
    print("=== 5ENDLESS FINAL TEST VERSION - NO PAUSE STARTED ===")
    # 1. Two explanation pages at the start
    for i in range(2):
        print(f"[5ENDLESS] Clicking explanation page {i+1}/2 at start...")
        click_button()
        time.sleep(1.5)

    # Q1: Single choice
    print("[5ENDLESS] Q1: Selecting answer using updated coordinates...")
    pyautogui.moveTo(906, 661)
    pyautogui.click()
    print("[5ENDLESS] Q1: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q1: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q2: Single choice with image recognition
    print("[5ENDLESS] Q2: Using image recognition...")
    try:
        click_image('Q2_answer.png', confidence=0.85)
    except:
        print("[5ENDLESS] Q2: Image not found, using fallback coordinates...")
        pyautogui.moveTo(952, 532)
        pyautogui.click()
    print("[5ENDLESS] Q2: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q2: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q3: Fill-in-the-blank
    print("[5ENDLESS] Q3: Fill-in-the-blank...")
    pyautogui.moveTo(1069, 595)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.typewrite("notice", interval=0.12)
    print("[5ENDLESS] Q3: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q3: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q4: Multi-blank (robust, single screen)
    print("[5ENDLESS] Q4: Multi-blank question...")
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ4please.png', (820, 879)),
        ('PNJ/PNJQ4kind.png', (917, 879)),
        ('PNJ/PNJQ4discuss.png', (1068, 885)),
    ], "Q4")
    print("[5ENDLESS] Q4: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q4: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q5: Multi-blank (robust, single screen)
    print("[5ENDLESS] Q5: Multi-blank question...")
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ5welcom,sir..png', (1256, 885)),
        ('PNJ/PNJQ5construction permit requests..png', (1007, 879)),
        ('PNJ/PNJQ5The Resident Architect SGPL.png', (753, 886)),
    ], "Q5")
    print("[5ENDLESS] Q5: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q5: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q6: Multi-blank (robust, single screen)
    print("[5ENDLESS] Q6: Multi-blank question...")
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ6Constrcution or Building permits.png', (553, 883)),
        ('PNJ/PNJQ6are written authorizations issued by.png', (1136, 884)),
        ('PNJ/PNJQ6a city or local government agency.png', (928, 886)),
        ('PNJ/PNJQ6to construct a project.png', (1329, 894)),
    ], "Q6")
    print("[5ENDLESS] Q6: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q6: Continuer...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Clicking middle explanation/info page after Q6...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # === NO PAUSE - CONTINUE IMMEDIATELY ===
    print("[5ENDLESS] Continuing immediately - no pause for maximum speed!")

    # Q7: Single choice with image recognition
    print("[5ENDLESS] Q7: Using image recognition...")
    try:
        click_image('Q7_answer.png', confidence=0.85)
    except:
        print("[5ENDLESS] Q7: Image not found, using fallback coordinates...")
        pyautogui.moveTo(1249, 597)
        pyautogui.click()
    print("[5ENDLESS] Q7: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q7: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q8: Multiple answers with image recognition
    print("[5ENDLESS] Q8: Using image recognition for multiple answers...")
    try:
        click_image('Q8_answer1.png', confidence=0.85)
        time.sleep(0.5)
        click_image('Q8_answer2.png', confidence=0.85)
    except:
        print("[5ENDLESS] Q8: Images not found, using fallback coordinates...")
        pyautogui.moveTo(1268, 540)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(1258, 603)
        pyautogui.click()
    print("[5ENDLESS] Q8: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q8: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q9: Fill-in-the-blank (UPDATED COORDINATES)
    print("[5ENDLESS] Q9: Fill-in-the-blank...")
    pyautogui.moveTo(1379, 644)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.typewrite("improvement", interval=0.12)
    print("[5ENDLESS] Q9: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q9: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q10: Fill-in-the-blank - Fill with: Reforms, business, changes
    print("[5ENDLESS] Q10: Fill-in-the-blank with multiple words...")
    # Click on "Reforms" field and type
    try:
        click_image('Q10_reforms.png', confidence=0.85)
    except:
        pyautogui.moveTo(633, 191)  # Fallback for "Reforms"
        pyautogui.click()
    time.sleep(0.5)
    
    # Click on "business" field and type
    try:
        click_image('Q10_business.png', confidence=0.85)
    except:
        pyautogui.moveTo(838, 241)  # Fallback for "business"
        pyautogui.click()
    time.sleep(0.5)
    
    # Click on "changes" field and type
    try:
        click_image('Q10_changes.png', confidence=0.85)
    except:
        pyautogui.moveTo(683, 289)  # Fallback for "changes"
        pyautogui.click()
    time.sleep(0.5)
    print("[5ENDLESS] Q10: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q10: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q11: Match the columns
    print("[5ENDLESS] Q11: Match the columns...")
    # Match 1: "I believe you will find" -> "this information useful."
    try:
        click_image('Q11_match1.png', confidence=0.85)
    except:
        pyautogui.moveTo(425, 451)  # "this information useful."
        pyautogui.click()
    time.sleep(0.5)
    
    # Match 2: "Thank you for" -> "your time, sir."
    try:
        click_image('Q11_match2.png', confidence=0.85)
    except:
        pyautogui.moveTo(618, 451)  # "your time, sir."
        pyautogui.click()
    time.sleep(0.5)
    
    # Match 3: "Reforms are divided" -> "into two types."
    try:
        click_image('Q11_match3.png', confidence=0.85)
    except:
        pyautogui.moveTo(533, 451)  # "into two types."
        pyautogui.click()
    time.sleep(0.5)
    print("[5ENDLESS] Q11: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q11: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q12: Place words in correct order
    print("[5ENDLESS] Q12: Place words in correct order...")
    # Click in order: 1, 2, 3, 4
    # 1: "those that make it easier"
    try:
        click_image('Q12_option1.png', confidence=0.85)
    except:
        pyautogui.moveTo(605, 453)  # "those that make it easier"
        pyautogui.click()
    time.sleep(0.5)
    
    # 2: "to do business and"
    try:
        click_image('Q12_option2.png', confidence=0.85)
    except:
        pyautogui.moveTo(483, 453)  # "to do business and"
        pyautogui.click()
    time.sleep(0.5)
    
    # 3: "those changes that"
    try:
        click_image('Q12_option3.png', confidence=0.85)
    except:
        pyautogui.moveTo(729, 453)  # "those changes that"
        pyautogui.click()
    time.sleep(0.5)
    
    # 4: "make it more difficult to do business"
    try:
        click_image('Q12_option4.png', confidence=0.85)
    except:
        pyautogui.moveTo(333, 453)  # "make it more difficult to do business"
        pyautogui.click()
    time.sleep(0.5)
    print("[5ENDLESS] Q12: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q12: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q13: Fill-in-the-blank with multiple fields
    print("[5ENDLESS] Q13: Fill-in-the-blank with multiple fields...")
    # Fill "impacts" field
    try:
        click_image('Q13_impacts.png', confidence=0.85)
    except:
        pyautogui.moveTo(773, 231)  # "impacts" field
        pyautogui.click()
    time.sleep(0.5)
    
    # Fill "Stakeholder" field
    try:
        click_image('Q13_stakeholder.png', confidence=0.85)
    except:
        pyautogui.moveTo(662, 255)  # "Stakeholder" field
        pyautogui.click()
    time.sleep(0.5)
    
    # Fill "viability" field
    try:
        click_image('Q13_viability.png', confidence=0.85)
    except:
        pyautogui.moveTo(825, 306)  # "viability" field
        pyautogui.click()
    time.sleep(0.5)
    print("[5ENDLESS] Q13: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q13: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Final pages
    print("[5ENDLESS] Handling final pages...")
    for i in range(3):
        print(f"[5ENDLESS] Final page {i+1}/3...")
        click_button()
        time.sleep(1.5)
    
    # Rejouer l'activité button
    print("[5ENDLESS] Clicking 'Rejouer l'activité' button...")
    pyautogui.moveTo(800, 969)
    pyautogui.click()
    time.sleep(2)

    print("[5ENDLESS] ✅ One complete cycle finished!")

if __name__ == '__main__':
    # One-time authentication on first launch
    ensure_first_run_auth()
    while True:
        run_final_once()
        time.sleep(2)

def run_final_once():
    print("=== 5ENDLESS FINAL TEST VERSION - NO PAUSE STARTED ===")
    # 1. Two explanation pages at the start
    for i in range(2):
        print(f"[5ENDLESS] Clicking explanation page {i+1}/2 at start...")
        click_button()
        time.sleep(1.5)

    # Q1: Single choice
    print("[5ENDLESS] Q1: Selecting answer using updated coordinates...")
    pyautogui.moveTo(906, 661)
    pyautogui.click()
    print("[5ENDLESS] Q1: Valider...")
    click_button()
    time.sleep(1.5)
    print("[5ENDLESS] Q1: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # ... (identique à la version principale – copiez votre logique Q2→Q13)
    print("[5ENDLESS] Veuillez copier la logique Q2→Q13 depuis le dépôt principal si nécessaire.")

if __name__ == '__main__':
    ensure_first_run_auth()
    while True:
        run_final_once()
        time.sleep(2)
