"""
Optional LLM Integration for enhanced AI recommendations
Supports OpenAI GPT-4 or Claude for advanced insights
"""

import os
from config import USE_LLM, OPENAI_API_KEY

if USE_LLM:
    import openai
    openai.api_key = OPENAI_API_KEY


async def enhance_build_recommendation(build_data: dict, user_query: str) -> str:
    """
    Use LLM to enhance build recommendations with AI insights
    
    Args:
        build_data: The base build information
        user_query: The user's original question
        
    Returns:
        Enhanced recommendation string
    """
    if not USE_LLM:
        return None
    
    try:
        prompt = f"""You are a Diablo 4 expert. Here's a build recommendation:

Build: {build_data['name']}
Description: {build_data['description']}
Key Skills: {', '.join(build_data['key_skills'])}
Legendary Items: {', '.join(build_data['legendary_items'])}
Stats Priority: {', '.join(build_data['stats_priority'])}

User Asked: {user_query}

Provide a detailed, helpful response about this build with practical tips and optimization advice. Keep it under 500 characters."""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Diablo 4 build guide expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"LLM Error: {e}")
        return None


async def analyze_gear(gear_list: list, class_name: str) -> str:
    """
    Use LLM to analyze gear synergies
    
    Args:
        gear_list: List of gear items
        class_name: Diablo 4 class name
        
    Returns:
        Analysis string
    """
    if not USE_LLM:
        return None
    
    try:
        prompt = f"""Analyze this gear setup for a {class_name}:
        
Gear: {', '.join(gear_list)}

Provide a brief analysis of synergies and suggestions. Keep it under 300 characters."""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Diablo 4 gear expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"LLM Error: {e}")
        return None


async def get_build_tips(build_name: str, difficulty_level: str) -> str:
    """
    Get AI-generated tips for playing a build
    
    Args:
        build_name: Name of the build
        difficulty_level: How hard the build is to play
        
    Returns:
        Tips string
    """
    if not USE_LLM:
        return None
    
    try:
        prompt = f"""Give me 3-4 practical tips for playing the '{build_name}' build effectively.
Difficulty level: {difficulty_level}

Keep each tip concise (1-2 sentences). Format as a numbered list."""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Diablo 4 build expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"LLM Error: {e}")
        return None