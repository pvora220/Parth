import asyncio

from backend.ai.agent import AIAgent


async def main():
    print("=====================================")
    print("   OSINT CYBER INTELLIGENCE PLATFORM ")
    print("=====================================")
    target = input("\nEnter username/email: ")

    report = await AIAgent().investigate(target)

    print("\n=========== REPORT ===========\n")
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
