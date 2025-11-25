"""
Enhanced messaging module with proper validation and error handling.
Supports Philippine phone numbers by default and real SMS provider integration.
"""
from typing import Optional, Dict
import re
from dataclasses import dataclass

@dataclass
class MessageResult:
    success: bool
    message: str
    provider: str
    message_id: Optional[str] = None

def validate_phone_number(phone: str) -> bool:
    """Validate phone number format (supports Philippine numbers)."""
    # Remove any whitespace, dashes, or parentheses
    clean_number = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Philippine mobile numbers: 09XX-XXX-XXXX or 9XX-XXX-XXXX
    ph_pattern = r'^(63|0)?9\d{9}$'
    # International format
    intl_pattern = r'^\d{10,15}$'
    
    return bool(re.match(ph_pattern, clean_number) or re.match(intl_pattern, clean_number))

def validate_message(message: str) -> bool:
    """Validate message content."""
    return bool(message and 1 <= len(message.strip()) <= 1600)

def format_phone_number(phone: str) -> str:
    """Format phone number to E.164 format (defaults to PH)."""
    # Remove formatting characters
    clean_number = re.sub(r'[\s\-\(\)\+]', '', phone)
    
    # Handle Philippine numbers
    if clean_number.startswith('09'):
        # 09XX-XXX-XXXX -> +639XXXXXXXXX
        clean_number = '+63' + clean_number[1:]
    elif clean_number.startswith('9') and len(clean_number) == 10:
        # 9XX-XXX-XXXX -> +639XXXXXXXXX
        clean_number = '+63' + clean_number
    elif clean_number.startswith('63') and len(clean_number) == 12:
        # 639XXXXXXXXX -> +639XXXXXXXXX
        clean_number = '+' + clean_number
    elif not clean_number.startswith('+'):
        # Default to PH if no country code
        if len(clean_number) == 10 and clean_number[0] == '9':
            clean_number = '+63' + clean_number
        else:
            clean_number = '+63' + clean_number
    
    return clean_number

def send_via_semaphore(api_key: str, recipient: str, message: str) -> MessageResult:
    """Send SMS via Semaphore (Philippine SMS provider)."""
    try:
        import requests
        
        formatted_number = format_phone_number(recipient)
        
        url = "https://api.semaphore.co/api/v4/messages"
        payload = {
            'apikey': api_key,
            'number': formatted_number,
            'message': message,
            'sendername': 'SEMAPHORE'
        }
        
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        
        result = response.json()
        
        if result and len(result) > 0:
            msg_data = result[0]
            if msg_data.get('status') == 'success' or msg_data.get('message_id'):
                return MessageResult(
                    success=True,
                    message=f"Message sent successfully to {formatted_number}",
                    provider="semaphore",
                    message_id=str(msg_data.get('message_id'))
                )
        
        return MessageResult(
            success=False,
            message=f"Failed to send: {result}",
            provider="semaphore"
        )
        
    except ImportError:
        return MessageResult(
            success=False,
            message="requests library not installed. Run: pip install requests",
            provider="semaphore"
        )
    except Exception as e:
        return MessageResult(
            success=False,
            message=f"Semaphore error: {str(e)}",
            provider="semaphore"
        )

def send_via_twilio(
    account_sid: str,
    auth_token: str,
    from_number: str,
    to_number: str,
    body: str
) -> MessageResult:
    """Send message via Twilio."""
    try:
        from twilio.rest import Client
        client = Client(account_sid, auth_token)
        
        # Format numbers
        to_number = format_phone_number(to_number)
        
        # Send message
        response = client.messages.create(
            body=body,
            from_=from_number,
            to=to_number
        )
        
        return MessageResult(
            success=True,
            message=f"Message sent successfully to {to_number}",
            provider="twilio",
            message_id=response.sid
        )
        
    except ImportError:
        return MessageResult(
            success=False,
            message="Twilio SDK not installed. Run: pip install twilio",
            provider="twilio"
        )
    except Exception as e:
        return MessageResult(
            success=False,
            message=f"Twilio error: {str(e)}",
            provider="twilio"
        )

def send_message_simulator(recipient: str, message: str) -> MessageResult:
    """Simulate sending an SMS message."""
    try:
        recipient = (recipient or "").strip()
        message = (message or "").strip()

        # Validation
        if not recipient:
            return MessageResult(False, "Recipient is required", "simulator")
        if not message:
            return MessageResult(False, "Message body is required", "simulator")
        if not validate_phone_number(recipient):
            return MessageResult(False, "Invalid phone number format. Use: 09XXXXXXXXX or +639XXXXXXXXX", "simulator")
        if not validate_message(message):
            return MessageResult(False, "Message must be between 1-1600 characters", "simulator")

        # Format phone number
        formatted_number = format_phone_number(recipient)
        
        # Simulate message sending
        message_id = f"SIM_{hash(formatted_number + message) % 100000:05d}"
        return MessageResult(
            success=True,
            message=f"✓ Message simulated for {formatted_number}",
            provider="simulator",
            message_id=message_id
        )

    except Exception as e:
        return MessageResult(
            success=False,
            message=f"Simulation error: {str(e)}",
            provider="simulator"
        )

def send_message(
    recipient: str,
    message: str,
    provider: str = "simulator",
    config: Optional[Dict[str, str]] = None
) -> MessageResult:
    """
    Send an SMS message using specified provider.
    
    Args:
        recipient: Destination phone number (PH format: 09XXXXXXXXX or +639XXXXXXXXX)
        message: Message content (max 1600 characters)
        provider: SMS provider ('simulator', 'semaphore', 'twilio')
        config: Provider configuration dictionary
    
    Returns:
        MessageResult object containing status and details
        
    Example usage:
        # Simulator (default)
        result = send_message("09171234567", "Hello World!")
        
        # Semaphore (Philippine SMS provider)
        config = {'api_key': 'your_semaphore_api_key'}
        result = send_message("09171234567", "Hello!", "semaphore", config)
        
        # Twilio
        config = {
            'account_sid': 'your_sid',
            'auth_token': 'your_token',
            'from_number': '+1234567890'
        }
        result = send_message("09171234567", "Hello!", "twilio", config)
    """
    try:
        # Validate inputs
        recipient = (recipient or "").strip()
        message = (message or "").strip()
        
        if not recipient or not message:
            return MessageResult(
                success=False,
                message="Both recipient and message are required",
                provider=provider
            )
        
        if not validate_phone_number(recipient):
            return MessageResult(
                success=False,
                message="Invalid phone number. Use PH format: 09XXXXXXXXX",
                provider=provider
            )
        
        if not validate_message(message):
            return MessageResult(
                success=False,
                message="Message must be between 1-1600 characters",
                provider=provider
            )
        
        # Route to appropriate provider
        if provider.lower() == "semaphore":
            if not config or 'api_key' not in config:
                return MessageResult(
                    success=False,
                    message="Semaphore API key required in config",
                    provider="semaphore"
                )
            return send_via_semaphore(config['api_key'], recipient, message)
            
        elif provider.lower() == "twilio":
            if not config:
                return MessageResult(
                    success=False,
                    message="Twilio configuration required",
                    provider="twilio"
                )
            required_keys = {'account_sid', 'auth_token', 'from_number'}
            if not all(key in config for key in required_keys):
                return MessageResult(
                    success=False,
                    message="Missing Twilio credentials (account_sid, auth_token, from_number)",
                    provider="twilio"
                )
            return send_via_twilio(
                config["account_sid"],
                config["auth_token"],
                config["from_number"],
                recipient,
                message
            )
        else:
            # Default to simulator
            return send_message_simulator(recipient, message)
            
    except Exception as e:
        return MessageResult(
            success=False,
            message=f"Unexpected error: {str(e)}",
            provider=provider
        )


# Configuration helper
def get_sms_config(provider: str = "semaphore") -> Dict[str, str]:
    """
    Get SMS configuration. Update this with your actual credentials.
    
    For Semaphore (Philippine SMS provider):
    1. Sign up at https://semaphore.co/
    2. Get your API key from dashboard
    3. Add it to the config below
    
    For Twilio:
    1. Sign up at https://www.twilio.com/
    2. Get Account SID and Auth Token
    3. Get a Twilio phone number
    4. Add them to the config below
    """
    configs = {
        "semaphore": {
            "api_key": "YOUR_SEMAPHORE_API_KEY_HERE"  # Get from https://semaphore.co/
        },
        "twilio": {
            "account_sid": "YOUR_TWILIO_ACCOUNT_SID",
            "auth_token": "YOUR_TWILIO_AUTH_TOKEN",
            "from_number": "+1234567890"  # Your Twilio phone number
        }
    }
    
    return configs.get(provider, {})