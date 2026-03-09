import asyncio

from backend.ai.agent import AIAgent


async def main():
    print("OSINT INTELLIGENCE PLATFORM")
    target = input("Enter target username/email: ")
    report = await AIAgent().investigate(target)
    print("\nREPORT")
    print(report)


if __name__ == "__main__":
    asyncio.run(main())
