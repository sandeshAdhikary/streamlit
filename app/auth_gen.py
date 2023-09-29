import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['AppKhola']).generate()
print(hashed_passwords)