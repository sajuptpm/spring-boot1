import openpyxl

wb = openpyxl.load_workbook('workflow-fixes/data1.xlsx', data_only=True)
ws = wb['spring_boot']

print(f"Sheet dimensions: max_row={ws.max_row}, max_column={ws.max_column}")

# 1. Header check
headers = [ws.cell(1, c).value for c in range(1, 46)]
print(f"Headers count: {len(headers)}")
for i, h in enumerate(headers, 1):
    if not h:
        print(f"ERROR: Header {i} is empty!")
    else:
        print(f"  Col {i}: {h}")

# 2. Check empty cells in data rows
empty_cells = []
for r in range(2, ws.max_row + 1):
    for c in range(1, 46):
        val = ws.cell(r, c).value
        if val is None or val == "":
            empty_cells.append((r, c, headers[c-1]))

print(f"\nTotal empty data cells across 84 rows x 45 columns: {len(empty_cells)}")
if empty_cells:
    for r, c, h in empty_cells[:10]:
        print(f"  Empty at Row {r}, Col {c} ({h})")

# 3. Check Category column (Infra vs Tool)
category_counts = {}
for r in range(2, ws.max_row + 1):
    cat = ws.cell(r, 2).value # Col 2: Category
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nCategory (Infra / Tool) Breakdown:")
for k, v in sorted(category_counts.items()):
    print(f"  {k}: {v}")

# 4. Check Pipeline Stage column
stage_counts = {}
for r in range(2, ws.max_row + 1):
    stg = ws.cell(r, 21).value # Col 21: Pipeline Stage
    stage_counts[stg] = stage_counts.get(stg, 0) + 1

print("\nPipeline Stage Breakdown:")
for k, v in sorted(stage_counts.items()):
    print(f"  {k}: {v}")

# 5. Check Record Type counts
upstream_count = 0
alternate_count = 0
for r in range(2, ws.max_row + 1):
    rec_type = ws.cell(r, 5).value # Col 5: Record Type
    if rec_type == 'Upstream Original Tool':
        upstream_count += 1
    elif rec_type == 'Recommended Fork Alternate':
        alternate_count += 1
    else:
        print(f"Unknown record type at row {r}: {rec_type}")

print(f"\nRecord Types: Upstream={upstream_count}, Alternates={alternate_count}, Total={upstream_count + alternate_count}")

# 6. Check Code Signing row
cs_rows = [r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value == 'code-signing service']
for r in cs_rows:
    print(f"\nVerification of Row {r} (code-signing service):")
    print(f"  Col 1 (Name): {ws.cell(r, 1).value}")
    print(f"  Col 2 (Category): {ws.cell(r, 2).value}")
    print(f"  Col 3 (Version): {ws.cell(r, 3).value}")
    print(f"  Col 9 (Free/Paid): {ws.cell(r, 9).value}")
    print(f"  Col 19 (Selected Sub): {ws.cell(r, 19).value}")
    print(f"  Col 30 (Required to Purchase?): {ws.cell(r, 30).value}")
    print(f"  Col 44 (Issues in ML): {ws.cell(r, 44).value}")

# 7. Check Automation Identity row
ai_rows = [r for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value == 'automation identity']
for r in ai_rows:
    print(f"\nVerification of Row {r} (automation identity):")
    print(f"  Col 1 (Name): {ws.cell(r, 1).value}")
    print(f"  Col 2 (Category): {ws.cell(r, 2).value}")
    print(f"  Col 3 (Version): {ws.cell(r, 3).value}")
    print(f"  Col 9 (Free/Paid): {ws.cell(r, 9).value}")
    print(f"  Col 19 (Selected Sub): {ws.cell(r, 19).value}")
    print(f"  Col 27 (Token): {ws.cell(r, 27).value}")
    print(f"  Col 30 (Required to Purchase?): {ws.cell(r, 30).value}")
    print(f"  Col 44 (Issues in ML): {ws.cell(r, 44).value}")

# 8. Check Required to Purchase breakdown
po_counts = {}
for r in range(2, ws.max_row + 1):
    val = ws.cell(r, 30).value
    po_counts[val] = po_counts.get(val, 0) + 1

print("\nRequired to Purchase Breakdown:")
for k, v in sorted(po_counts.items()):
    print(f"  {k}: {v}")
