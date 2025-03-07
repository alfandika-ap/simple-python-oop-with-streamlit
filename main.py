import streamlit as st
import pandas as pd
from libs import StreamingPlatform, Member

PLATFORM_NAME = "Banana Music"

if "streaming_platform" not in st.session_state:
    st.session_state.streaming_platform = StreamingPlatform(PLATFORM_NAME)

if "mode" not in st.session_state:
    st.session_state.mode = {}

st.title(f"Welcome to, {PLATFORM_NAME}")

page = st.sidebar.selectbox("Menu", ["Add Member", "Manage Subcription", "View Subcription Members"])

if page == "Add Member":
    st.write("## Add Member")
    name = st.text_input("Name")
    button = st.button("Add Member")

    if button:
        new_member = Member(name)
        st.session_state.streaming_platform.register_member(new_member)
        name = ""
        st.rerun()

elif page == "Manage Subcription":
    st.write("## Manage Subcription")

    for index, member in enumerate(st.session_state.streaming_platform.members):

        if index > 0:
            st.write("--------------------")

        status = "Subscribed" if member.is_subcribed else "Not Subscribed"
        st.write(f"{member.name} - {status}")
        if member.is_subcribed:
            st.write(f"Duration: {member.subscription_duration} Day{"s" if member.subscription_duration > 1 else ""}")
        
        if member.is_subcribed:
            unsubscribe_btn = st.button("Unubscribe", key=f"unsub_{index}")
            if unsubscribe_btn:
                member.unsubcribe()
                st.session_state.mode[index] = ""
                st.rerun()

        elif member.is_subcribed == False:
            subscribe_btn = st.button("Subscribe", key=f"sub_{index}")
            if subscribe_btn:
                st.session_state.mode[index] = "unsubcribe"
        
        if st.session_state.mode.get(index) == "unsubcribe":
            

            duration_subcription = st.number_input("Duration Subcription", min_value=1, step=1)
            tc1, tc2, _= st.columns([2,2,12])

            with tc1:
                discard_subcription_btn = st.button("Cancel")
                if discard_subcription_btn:
                    st.session_state.mode[index] = ""
                    st.rerun()

            with tc2:
                save_subcription_btn = st.button("Save")
                if save_subcription_btn: 
                    member.subcribe(duration_subcription)
                    st.session_state.mode[index] = ""
                    st.rerun()

elif page == "View Subcription Members":
    if not st.session_state.streaming_platform.members:
        st.write("No current members")
    else:
        subcription_members = st.session_state.streaming_platform.get_subcription_member()
        members_data = []
        for index, member in enumerate(subcription_members, start=1):
            members_data.append({
                "No": f"{index}",
                "Name": member.name,
                "Duration": f"{member.subscription_duration} Day{"s" if member.subscription_duration > 1 else ""}"
            })
            df = pd.DataFrame(members_data)
            st.table(df)