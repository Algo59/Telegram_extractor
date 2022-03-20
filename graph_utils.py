def topic_checker_util(row):
    if "לבנון" in row['Content']:
        row['Topic'] = "לבנון"
        return row
    elif "איראן" in row['Content']:
        row['Topic'] = "איראן"
        return row
    elif "ישראל" in row['Content']:
        row['Topic'] = "ישראל"
        return row
    elif "רוסיה" in row['Content'] or "רוסי" in row['Content']:
        row['Topic'] = "רוסיה"
        return row
    elif "חיזבאלה" in row['Content']:
        row['Topic'] = "חיזבאללה"
        return row
    elif "פיגוע" in row['Content']:
        row['Topic'] = "פיגוע דקירה"
        return row
    elif "Ukrainian" in row['Content'] or "אוקראינה" in row['Content'] or "קייב" in row['Content']:
        row['Topic'] = "אוקראינה"
        return row
    elif "הרב" in row['Content'] or "בני ברק" in row['Content']:
        row['Topic'] = "הרב שמת"
        return row
    else:
        return row