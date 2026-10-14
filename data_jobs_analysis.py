
import pandas as pd
import matplotlib.pyplot as plt

# Lae andmestik
df = pd.read_csv("Cleaned_DS_Jobs.csv")

# --- Andmestiku kirjeldus ---
print("📊 Andmestiku kirjeldus")
print(f"Ridade arv: {df.shape[0]}")
print(f"Veergude arv: {df.shape[1]}")
print("\nAndmetüübid:")
print(df.dtypes)
print("\nUnikaalsete väärtuste arv iga veeru kohta:")
print(df.nunique())
print("\nEsimesed read:")
print(df.head())

# --- Päringud ja rühmitamised ---

# 1. Keskmine palk osariikide lõikes (Top 10)
avg_salary_by_state = df.groupby("job_state")["avg_salary"].mean().sort_values(ascending=False).head(10)

# 2. Tööde arv tehnoloogiate põhjal
tech_skills = ['python', 'excel', 'hadoop', 'spark', 'aws', 'tableau', 'big_data']
tech_counts = df[tech_skills].sum().sort_values(ascending=False)

# 3. Palk ettevõtte vanuse rühmade lõikes
company_age_grouped = df.groupby(pd.cut(df["company_age"], bins=[0,10,20,30,40,50,60,70,100]))["avg_salary"].mean()

# 4. Kõrgeima keskmise palgaga ametinimetused (Top 10)
top_roles = df.groupby("Job Title")["avg_salary"].mean().sort_values(ascending=False).head(10)

# 5. Seniority ja tööde arv
seniority_counts = df["seniority"].value_counts()

# --- Visualiseeringud ---

# Graafik 1: Keskmine palk osariikide lõikes
plt.figure(figsize=(10,6))
avg_salary_by_state.plot(kind="bar", color="steelblue")
plt.title("Keskmine palk osariikide lõikes (Top 10)")
plt.ylabel("Keskmine palk")
plt.xlabel("Osariik")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Graafik 2: Tehnoloogiate nõudlus
plt.figure(figsize=(10,6))
tech_counts.plot(kind="bar", color="orange")
plt.title("Tehnoloogiate nõudlus töökuulutustes")
plt.ylabel("Tööde arv")
plt.xlabel("Tehnoloogia")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Graafik 3: Palk ettevõtte vanuse rühma lõikes
plt.figure(figsize=(10,6))
company_age_grouped.plot(kind="bar", color="green")
plt.title("Keskmine palk ettevõtte vanuse lõikes")
plt.ylabel("Keskmine palk")
plt.xlabel("Ettevõtte vanuse rühm")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Graafik 4: Kõrgeima keskmise palgaga ametid
plt.figure(figsize=(10,6))
top_roles.plot(kind="bar", color="purple")
plt.title("Top 10 ametit keskmise palga järgi")
plt.ylabel("Keskmine palk")
plt.xlabel("Ametinimetus")
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Graafik 5: Tööde jaotus seniority järgi
plt.figure(figsize=(8,5))
seniority_counts.plot(kind="bar", color="red")
plt.title("Tööde jaotus seniority järgi")
plt.ylabel("Tööde arv")
plt.xlabel("Seniority")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
