# Methods

## Scope
Statistics a homeowner, journalist or researcher would look up about hard water and residential drinking water in the United States, plus a small set of global drinking water access figures. Sections: hardness by region and city, how many homes have hard water, softener and home treatment adoption, effects on water heaters and appliances, public water system violations, lead service lines, PFAS, private wells (nitrate and arsenic), salt use for water softening, chloride and softener regulation, consumer concern, and global access.

## Source selection
Primary sources were preferred: federal and state agencies (USGS, U.S. EPA, state environmental agencies), utilities, universities, peer-reviewed or government-funded studies, and the original publisher of any survey. Widely repeated figures were traced to their origin. Where no primary source could be found, the figure was left out, and the gap is stated in the data instead of repeating the unsourced number.

## Verification (Oct 11, 2026)
1. Every source URL was fetched on 2026-10-11 with a browser user agent. HTML was converted to text and PDFs with `pdftotext -layout`. Spreadsheet tables were read from the original file.
2. Each statistic's exact quote or table value was matched, with whitespace normalized, against the fetched text. Statistics that didn't match were rewritten to what the source says, or dropped. The final pass reported 0 mismatches.
3. Each source's publisher, title and own date were recorded, along with the retrieval date.
4. A live check confirmed that every source URL returned HTTP 200 at build time.

The research ledger, with SHA-256 hashes of the fetched files, is kept by Water System Guide.

## Limitations
- This is a compilation of published figures, not new measurements and not a statistical sample.
- Figures differ in year, method, unit and geography. Read `source_date` and the source before comparing rows.
- Source pages can change after retrieval. The `retrieved` date is when the wording was checked.

## License
The compilation (selection, arrangement, wording of rows and column structure) is released under CC BY 4.0, with credit to Water System Guide. Underlying facts belong to their publishers. Cite the original source for any individual figure.
