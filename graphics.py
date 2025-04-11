
def draw_logo():
    svg_code = """
    <div style="height: 50vh; display: flex; justify-content: center; align-items: center; pointer-events: none; position: static;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 350">
      <!-- Transparent background -->
      <rect width="600" height="350" fill="none" />
      
      <!-- Stars in background -->
      <g>
        <circle cx="50" cy="50" r="1.5" fill="#E0E0E0" opacity="0.8" />
        <circle cx="120" cy="80" r="1" fill="#E0E0E0" opacity="0.6" />
        <circle cx="200" cy="40" r="1.2" fill="#E0E0E0" opacity="0.7" />
        <circle cx="280" cy="90" r="1" fill="#E0E0E0" opacity="0.8" />
        <circle cx="350" cy="30" r="1.5" fill="#E0E0E0" opacity="0.7" />
        <circle cx="420" cy="70" r="1" fill="#E0E0E0" opacity="0.6" />
        <circle cx="490" cy="50" r="1.2" fill="#E0E0E0" opacity="0.8" />
        <circle cx="550" cy="100" r="1.3" fill="#E0E0E0" opacity="0.7" />
        <circle cx="70" cy="150" r="1" fill="#E0E0E0" opacity="0.6" />
        <circle cx="150" cy="190" r="1.2" fill="#E0E0E0" opacity="0.8" />
        <circle cx="350" cy="170" r="1" fill="#E0E0E0" opacity="0.7" />
        <circle cx="450" cy="220" r="1.4" fill="#E0E0E0" opacity="0.6" />
        <circle cx="500" cy="320" r="1" fill="#E0E0E0" opacity="0.8" />
        <circle cx="70" cy="300" r="1.2" fill="#E0E0E0" opacity="0.7" />
        <circle cx="150" cy="330" r="1.5" fill="#E0E0E0" opacity="0.8" />
        <circle cx="400" cy="290" r="1.3" fill="#E0E0E0" opacity="0.7" />
      </g>
      
      <!-- Sun comet body with gradient -->
      <linearGradient id="sunGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FFA000" />
        <stop offset="50%" stop-color="#FFEB3B" />
        <stop offset="100%" stop-color="#FFF176" />
      </linearGradient>
      
      <!-- Comet trail -->
      <defs>
        <linearGradient id="cometTrail" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0" />
          <stop offset="40%" stop-color="#FFF176" stop-opacity="0.4" />
          <stop offset="70%" stop-color="#FFEB3B" stop-opacity="0.6" />
          <stop offset="100%" stop-color="#FFA000" stop-opacity="0.8" />
        </linearGradient>
      </defs>
      
      <!-- Path showing upward curved trajectory with the tail going down -->
      <path d="M150,300 C250,200 350,150 450,130" fill="none" stroke="url(#cometTrail)" stroke-width="80" stroke-linecap="round" />
      
      <!-- Small particles in the trail -->
      <g>
        <circle cx="200" cy="265" r="2" fill="#FFF59D" />
        <circle cx="250" cy="230" r="1.5" fill="#FFF59D" />
        <circle cx="300" cy="195" r="2.2" fill="#FFF59D" />
        <circle cx="350" cy="170" r="1.8" fill="#FFF59D" />
        <circle cx="400" cy="150" r="1.5" fill="#FFF59D" />
        <circle cx="430" cy="140" r="1.2" fill="#FFF59D" />
      </g>
      
      <!-- Sun core - positioned at upper right -->
      <circle cx="450" cy="130" r="40" fill="url(#sunGradient)" />
      
      <!-- Sun rays -->
      <g>
        <path d="M450,90 L450,70" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M450,170 L450,190" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M410,130 L390,130" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M490,130 L510,130" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M420,100 L410,90" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M480,100 L490,90" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M420,160 L410,170" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
        <path d="M480,160 L490,170" stroke="#FFEB3B" stroke-width="3" stroke-linecap="round" />
      </g>
    </svg>
    </div>
    """

    return svg_code


def build_icon():

    # Put import here so streamlit server does not try and import and crash
    from cairosvg import svg2png

    svg_code = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192">
      <!-- Transparent background -->
      <rect width="192" height="192" fill="none" />
    
      <!-- Sun gradient -->
      <linearGradient id="sunGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#FFA000" />
        <stop offset="50%" stop-color="#FFEB3B" />
        <stop offset="100%" stop-color="#FFF176" />
      </linearGradient>
    
      <!-- Sun core - centered and full size -->
      <circle cx="96" cy="96" r="70" fill="url(#sunGradient)" />
    
      <!-- Sun rays - positioned around the sun -->
      <g>
        <!-- Vertical rays -->
        <path d="M96,26 L96,6" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
        <path d="M96,166 L96,186" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
    
        <!-- Horizontal rays -->
        <path d="M26,96 L6,96" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
        <path d="M166,96 L186,96" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
    
        <!-- Diagonal rays -->
        <path d="M50,50 L36,36" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
        <path d="M142,50 L156,36" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
        <path d="M50,142 L36,156" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
        <path d="M142,142 L156,156" stroke="#FFEB3B" stroke-width="5" stroke-linecap="round" />
    
        <!-- Additional rays for fuller appearance -->
        <path d="M70,34 L62,20" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M122,34 L130,20" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M34,70 L20,62" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M158,70 L172,62" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M34,122 L20,130" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M158,122 L172,130" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M70,158 L62,172" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
        <path d="M122,158 L130,172" stroke="#FFEB3B" stroke-width="4" stroke-linecap="round" />
      </g>
    </svg>
    """

    png_data = svg2png(bytestring=svg_code.encode(), output_width=192,
                       output_height=192)

    # Save as PNG for favicon
    with open("favicon.png", "wb") as f:
        f.write(png_data)


def apply_chart_formatting(chart, show_legend=True , yaxes_title=None, height=None):
    chart.update_layout(
        # height=200,
        margin={
            't': 20,
            'b': 20,
        },
        legend=dict(
            font=dict(size=18)
        ),
        legend_title_text=""
    )
    chart.update_xaxes(
        tickfont=dict(size=18),
        title_font=dict(size=18),
        title_text=""
    )
    chart.update_yaxes(
        tickfont=dict(size=18),
        title_font=dict(size=18),
    )

    if yaxes_title is not None:
        chart.update_yaxes(
            title_text=yaxes_title
        )

    if not show_legend:
        chart.update_layout(showlegend=False)

    if height:
        chart.update_layout(height=height)