# Visuals

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
from variance_analysis import df, material_df


# Line chart on sales over months

revenues = df[df["Line_Item"] == "Revenue"]


plt.plot(revenues["Month"], revenues["signed_pct_variance"], marker = 'o')
plt.xlabel('Months')
plt.ylabel('Revenue Variance (%)')
plt.title('Sales Department Monthly Variances')
plt.xticks(rotation = 45)
plt.axhline(0, color = 'black', linewidth = 0.8)

plt.fill_between(revenues["Month"], revenues["signed_pct_variance"], 0,
                 where = (revenues["signed_pct_variance"] >= 0),
                          color = 'green', alpha = 0.3, interpolate = True)

plt.fill_between(revenues["Month"], revenues["percentage_variance"], 0,
                 where = (revenues["percentage_variance"] < 0),
                 color = 'red', alpha = 0.3, interpolate = True)

plt.show()


# Bar chart on costs between departments

costs_df = df[df["Line_Item"] != "Revenue"]

department_summary = costs_df.groupby('Department')[['Budget', 'Actual']].sum()
print(department_summary)

department_summary[["Budget", "Actual"]].plot(
    kind = 'bar',
    color = ["#1f3a5f", "#a0a0a0"])
plt.title("Department Costs: Budgeted vs Actual")
plt.ylabel("Cost")
plt.xticks(rotation = 360)
plt.ticklabel_format(style = 'plain', axis = 'y')

ax = plt.gca()
ax.yaxis.set_major_locator(ticker.MultipleLocator(250000))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"£{x:,.0f}"))
plt.show()


# Pie charts showing composition ot total budgeted and actual spent

fig, axes = plt.subplots(1, 2, figsize = (12, 6))

axes[0].pie(department_summary["Budget"], labels = department_summary.index, autopct = '%1.1f%%')
axes[0].set_title('Budgeted Cost Composition by Department')


axes[1].pie(department_summary["Actual"], labels = department_summary.index, autopct = '%1.1f%%')
axes[1].set_title('Actual Cost Composition by Department')

plt.show()




