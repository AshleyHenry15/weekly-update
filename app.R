library(shiny)
library(quarto)

# Define UI for the Shiny app
ui <- fluidPage(
  titlePanel("Weekly GitHub Activity Report"),
  
  # Include the Quarto-generated HTML report
  mainPanel(
    # Display the HTML report as a Shiny UI component
    includeHTML("activity_report.html")  # Path to your Quarto report
  )
)

# Define server logic (optional, depending on interactivity needed)
server <- function(input, output) {
  # You can add additional interactive features if desired.
}

# Run the Shiny app
shinyApp(ui = ui, server = server)
