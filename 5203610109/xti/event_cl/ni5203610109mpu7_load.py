#
# NICER Observation 5203610109
# nicerl3-spect 1.7
# Run date: Thu Jun 22 20:23:34 2023
# Observation: 5203610109
#
#BEGIN
AllData("1:1 5203610109/xti/event_cl/ni5203610109mpu7_sr.pha")
spec1 = AllData(1)
spec1.ignore("bad")
spec1.background = "5203610109/xti/event_cl/ni5203610109mpu7_bg.pha"
spec1.response = "5203610109/xti/event_cl/ni5203610109mpu7.rmf"
spec1.response.arf = "5203610109/xti/event_cl/ni5203610109mpu7.arf"
#END
