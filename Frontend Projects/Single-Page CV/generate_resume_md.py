import yaml 

with open('resume_content.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

lines = []

# Header
lines.append(f"# {data['name']}")
lines.append(f"**{data['title']}**\n")
lines.append(f"- Phone: {data['contact']['phone']}")
lines.append(f"- Email: [{data['contact']['email']}](mailto:{data['contact']['email']})")
lines.append(f"- [LinkedIn]({data['contact']['linkedin']})\n")

# Skills
lines.append("## Skills")
lines.append(f"- **Programming Languages & Frameworks:** {', '.join(data['skills']['programming_languages_and_frameworks'])}")
lines.append(f"- **Database Skills:** {', '.join(data['skills']['database_skills'])}")
lines.append(f"- **Automation Tools:** {', '.join(data['skills']['automation_tools'])}")
lines.append(f"- **Other Skills:** {', '.join(data['skills']['other_skills'])}\n")

# Experience
lines.append("## Experience")
for exp in data['experience']:
    lines.append(f"### {exp['title']} @ {exp['company']} ({exp['location']})")
    lines.append(f"*{exp['period']}*")
    for r in exp['responsibilities']:
        lines.append(f"- {r}")
    lines.append(f"**Tech Stack:** {', '.join(exp['tech_stack'])}\n")

# Certifications
lines.append("## Certifications")
for c in data['certifications']:
    lines.append(f"- {c}")

# Achievements
lines.append("\n## Achievements")
for a in data['achievements']:
    lines.append(f"- {a}")

# Education
lines.append("\n## Education")
lines.append("\n|||\n|--|--|")
for e in data['education']:
    lines.append(f"|**{e['degree']}**, {e['institution']} |({e.get('year', '')})|")

with open('SinglePageCV_V3.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))