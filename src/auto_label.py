import pandas as pd
import re

def auto_label(text):
    text = str(text).lower()
    
    # Kata kunci negatif
    neg_words = ['mati', 'padam', 'lama', 'jengkel', 'marah', 'rugi', 'buruk', 'kacau', 'protes', 'babi', 'anjing', 'bodoh', 'tolol', 'goblok', 'kecewa', 'parah', 'gila', 'hancur', 'susah', 'penderitaan']
    
    # Kata kunci positif
    pos_words = ['nyala', 'terang', 'makasih', 'alhamdulillah', 'cepat', 'sigap', 'terima kasih', 'baik', 'salut', 'mantap', 'bagus', 'pulih']
    
    neg_score = sum(1 for w in neg_words if re.search(r'\b' + w + r'\b', text))
    pos_score = sum(1 for w in pos_words if re.search(r'\b' + w + r'\b', text))
    
    if neg_score > pos_score:
        return 'negatif'
    elif pos_score > neg_score:
        return 'positif'
    else:
        return 'netral'

def main():
    path = 'data/raw/dataset_sumatera_blackout.csv'
    df = pd.read_csv(path)
    
    print(f"Total baris sebelum pelabelan: {len(df)}")
    
    df['label'] = df['text'].apply(auto_label)
    
    # Save back
    df.to_csv(path, index=False, encoding='utf-8')
    print("Distribusi sentimen hasil auto-label:")
    print(df['label'].value_counts())
    print("Selesai melabeli!")

if __name__ == '__main__':
    main()
