import speedtest

st = speedtest.Speedtest()
print("Download Speed:", st.download() / 1_000_000, "Mbps")
print("Upload Speed:", st.upload() / 1_000_000, "Mbps")
