def install_local(source):
    if os.path.isdir(source):
        # Check if the directory is an Agent Plugins layout
        if os.path.exists(os.path.join(source, 'SKILL.md')):
            # Install each skill in the directory
            for skill_dir in os.listdir(source):
                skill_path = os.path.join(source, skill_dir)
                if os.path.exists(os.path.join(skill_path, 'SKILL.md')):
                    # Install the skill
                    install_skill(skill_path)
        else:
            # Raise an error if the directory is not an Agent Plugins layout
            raise ValueError(f'Invalid Agent Plugins directory layout: {source}')
    elif os.path.isfile(source):
        # Install a standalone skill
        install_skill(source)
    else:
        # Raise an error if the source is neither a directory nor a file
        raise ValueError(f'Invalid source: {source}')