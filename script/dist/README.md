# Journal Digital Corpus Mapper DEMO

An interactive geographical visualization tool for corpus metadata. Displays dual heatmaps of location data with temporal animation capabilities.

## Funding Acknowledgment

This interface is part of the research project **'Modern Times 1936'** financed by the **Bank of Sweden Tercentenary Foundation** (Riksbankens Jubileumsfond, grant number **P21-0012**).

## About

This is a static website that visualizes geographical metadata from two sources:
- **JDC Speech**: Named entity recognition results from the Journal Digital Corpus
- **SMDB-SAB**: Location metadata from the Swedish Media Database

The visualization allows you to:
- View dual heatmaps of location mentions over time
- Animate through temporal data with a configurable moving window
- Search for specific locations
- View statistics and trends in the sidebar

## Usage

### Map Interaction
- **Pan**: Click and drag the map
- **Zoom**: Use mouse wheel or zoom controls
- **Toggle Layers**: Use checkboxes in the sidebar to show/hide each metadata set

### Timeline Controls
- **Play/Pause**: Animate through time automatically
- **Window Size**: Adjust the time window (in years) to aggregate data
- **Delay**: Set animation speed (seconds between steps)
- **Step Size**: Set how many years to advance per animation frame

### Search
- Type a location name in the search box
- Click on a result to focus the map on that location

### Statistics
- View location counts over time in the sidebar chart
- Drag the brush on the chart to change the current time window
- See breakdown by location type (city, village, etc.)

## Data Sources

### Journal Digital Corpus
Aspenskog, H., Johansson, M., & Nordström, L. (2025). *Journal Digital Corpus: A Swedish Newsreel Transcription Corpus*. Under review.

This visualization uses named entity recognition results extracted from Swedish newsreel transcriptions using the KB-BERT model.

### Svensk Mediedatabas (SMDB)
Location metadata extracted from the Swedish Media Database's SAB collection.

## Technology Stack

### Core Visualization Libraries
- **D3.js v7.8.5** (Bostock et al., 2011) - Data-driven visualization library for heatmaps and charts
- **Leaflet.js v1.9.4** (Agafonkin et al.) - Interactive mapping library

### Map Data & Geocoding
- **OpenStreetMap** (Haklay & Weber, 2008) - Collaborative open map data
- **Nominatim** (OpenStreetMap Foundation) - Geocoding service for location data
- **Geofabrik** - OpenStreetMap data extracts
- **Nominatim-Docker** (mediagis) - Containerized geocoding service

### Web Technologies
- **JavaScript/ECMAScript 2023** (Ecma International) - Programming language
- **HTML5** (W3C) - Document structure
- **CSS3** (W3C) - Styling and layout

### Build Tools
- **Vite v5.0** - Fast build tool and development server
- **Node.js** (OpenJS Foundation) - JavaScript runtime environment
- **npm** - Package manager
- **Python 3** (Van Rossum & Drake) - Data processing scripts

### NLP Tools
- **KB-BERT NER Model** (KB Labb, 2022) - Swedish named entity recognition for location extraction

### Development Assistance
- **Claude 4.5 Sonnet** (Anthropic, 2025) - AI language model
- **Claude Code** (Anthropic, 2025) - AI-powered development CLI

## Data Format

The application loads three JSON data files:

### Corpus Metadata Files
- `corpus-metadata-1.json`: JDC Speech location mentions by year
- `corpus-metadata-2.json`: SMDB-SAB location metadata by year

Each file contains an array of items with:
- `id` (string): Unique identifier
- `year` (number): Year associated with the item
- `locations` (array): Array of location IDs

### Locations File
- `locations.json`: Geocoded location data

Contains an object mapping location IDs to location details:
- `name` (string): Short location name
- `display_name` (string): Full display name
- `type` (string): Location type (building, village, city, region, province, country, continent)
- `lat` (number): Latitude coordinate
- `lon` (number): Longitude coordinate
- `boundingbox` (array, optional): Bounding box `[minLat, maxLat, minLon, maxLon]`

## Acknowledgments

This interface is part of the research project **'Modern Times 1936'** financed by the **Bank of Sweden Tercentenary Foundation** (Riksbankens Jubileumsfond, grant number **P21-0012**).

Developed collaboratively using Claude 4.5 Sonnet via Claude Code CLI.

## Source Code

The source code for this project is available in a separate repository. This repository contains only the built static website.

## License

MIT

## Contributing

For issues or suggestions, please use the GitHub issue tracker.
