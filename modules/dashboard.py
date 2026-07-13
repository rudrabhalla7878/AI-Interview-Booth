import streamlit as st
import plotly.graph_objects as go


def show_dashboard(
    technical,
    voice,
    stress,
    final_score
):

    st.markdown("## 📊 Performance Dashboard")

    # ===========================
    # BAR CHART
    # ===========================

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=[
                "Technical",
                "Voice",
                "Stress",
                "Final"
            ],

            y=[
                technical,
                voice,
                stress,
                final_score
            ],

            text=[
                f"{technical:.1f}",
                f"{voice:.1f}",
                f"{stress:.1f}",
                f"{final_score:.1f}"
            ],

            textposition="outside"

        )

    )

    fig.update_layout(

        height=450,

        title="Interview Performance",

        xaxis_title="Metrics",

        yaxis_title="Score",

        yaxis=dict(range=[0,100])

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ===========================
    # GAUGE CHART
    # ===========================

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=final_score,

            title={
                "text":"Final Interview Score"
            },

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "thickness":0.3
                },

                "steps":[

                    {

                        "range":[0,50],

                        "color":"#ffcccc"

                    },

                    {

                        "range":[50,75],

                        "color":"#fff3cd"

                    },

                    {

                        "range":[75,100],

                        "color":"#d4edda"

                    }

                ]

            }

        )

    )

    gauge.update_layout(

        height=400

    )

    st.plotly_chart(

        gauge,

        use_container_width=True

    )