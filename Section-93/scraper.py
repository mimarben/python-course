from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_nba_player_stats():
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.nba.com/stats/players/traditional")
    time.sleep(2)
    # Accept cookies if present
    try:
        accept_btn = driver.find_element(By.XPATH, '//button[text()="Accept All Cookies"]')
        accept_btn.click()
        WebDriverWait(driver, 2).until(EC.staleness_of(accept_btn))  # Wait for the button to disappear
        print("Accepted cookies.")
    except Exception as e:
        print(f"Cookie acceptance failed: {e}")

    # Wait for the page to load
    try:
        #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Crom_table__p1iZz")))
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.Crom_table__p1iZz tbody tr"))
        )
        print("Table loaded successfully.")
    except Exception as e:
        print(f"Error loading Table: {e}")
        driver.quit()
        return []


    
    # Wait for the table to be present
    players = []
    try:
        #rows = driver.find_elements(By.CSS_SELECTOR, ".Crom_table__p1iZz tbody tr")[:10]  # First 10 players  # First 10 players
        rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'Crom_table__p1iZz')]//tbody/tr")[:100]  # First 10 players
        print(f"Found {len(rows)} rows")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            print(f"Found {len(cols)} cols")
            print(cols)
            if cols:
                players.append({
                    "rank": cols[0].text,
                    "player": cols[1].text,
                    "team": cols[2].text,
                    "age": cols[3].text,
                    "games_played": cols[4].text,
                    "wins": cols[5].text,
                    "losses": cols[6].text,
                    "minutes": cols[7].text,
                    "points": cols[8].text,
                    "field_goals_made": cols[9].text,
                    "field_goals_attempted": cols[10].text,
                    "field_goal_percentage": cols[11].text,
                    "three_point_field_goals_made": cols[12].text,
                    "three_point_field_goals_attempted": cols[13].text,
                    "three_point_percentage": cols[14].text,
                    "free_throws_made": cols[15].text,
                    "free_throws_attempted": cols[16].text,
                    "free_throw_percentage": cols[17].text,
                    "offensive_rebounds": cols[18].text,
                    "defensive_rebounds": cols[19].text,
                    "total_rebounds": cols[20].text,
                    "assists": cols[21].text,
                    "turnovers": cols[22].text,
                    "steals": cols[23].text,
                    "blocks": cols[24].text,
                    "personal_fouls": cols[25].text,
                    "fantasy_points": cols[26].text,
                    "double_doubles": cols[27].text,
                    "triple_doubles": cols[28].text,
                    "plus_minus": cols[29].text
                })
    except Exception as e:
        print(f"Error while fetching player data: {e}")
    finally:
        driver.close()
        driver.quit()

    return players
