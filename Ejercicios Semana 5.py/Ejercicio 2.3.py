def calcular_horas_tiktok(minutos_por_día):
    minutos_totales = minutos_por_día * 7
    horas_totales = minutos_totales / 60
    return horas_totales

# Pruébala con diferentes valores
horas = calcular_horas_tiktok(30)  # 30 minutos por día
print(f"Ves {horas} horas de TikTok a la semana")

horas2 = calcular_horas_tiktok(60)  # 60 minutos por día
print(f"Ves {horas2} horas de TikTok a la semana")