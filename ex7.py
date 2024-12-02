def arrondir_notes(notes):
    notes_arrondies = []
    
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple = (note + 4) // 5 * 5
            if prochain_multiple - note < 3:
                notes_arrondies.append(prochain_multiple)
            else:
                notes_arrondies.append(note)
    
    return notes_arrondies

notes_etudiants = [33, 38, 42, 44, 56, 59, 61, 88, 91]

notes_finales = arrondir_notes(notes_etudiants)

for i in range(len(notes_finales)):
    if notes_finales[i] >= 40:
        print("l'etudiant a reussi")
    else:
        print("l'étudiant a échoué")