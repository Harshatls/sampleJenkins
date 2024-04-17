def before_scenario(context, scenario):
    context.config.setup_logging()

def after_scenario(context, scenario):
    context.driver.quit()
